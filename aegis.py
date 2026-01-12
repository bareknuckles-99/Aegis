import os
import argparse
from google import genai
from google.genai import types
import time

def run_audit(target_path):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    # 1. Recon: Collect and truncate code
    code_context = ""
    for root, _, files in os.walk(target_path):
        for file in files:
            if file.endswith(('.sol', '.vy', '.rs')):
                with open(os.path.join(root, file), 'r') as f:
                    code_context += f"\n--- FILE: {file} ---\n{f.read()[:20000]}\n"

    # 2. The Master Prompt
    prompt = f"""
    <role>Expert Smart Contract Security Researcher</role>
    <task>Audit this code for 100% exploitable bugs.</task>
    <context>{code_context}</context>
    <instructions>
    For EACH bug: Provide Severity, Description, and a Foundry PoC (.t.sol).
    Ensure the PoC is in a ```solidity code block.
    </instructions>
    """

    # 3. Execution
    for attempt in range(3):
        try:
            print(f"Starting Audit (Attempt {attempt+1}/3)...")
            response = client.models.generate_content(
                model="gemini-2.0-flash-thinking-exp", # Updated to the latest thinking model
                contents=prompt,
                config=types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(include_thoughts=True)
                )
            )
            
            # --- NEW: Save the report to a file for the dashboard ---
            with open("audit_report.md", "w") as f:
                f.write(response.text)

            # Send to GitHub UI Summary
            if os.getenv('GITHUB_STEP_SUMMARY'):
                with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as f:
                    f.write(response.text)
            
            print(response.text)

            # 4. Extract Exploit
            if "```solidity" in response.text:
                exploit_code = response.text.split("```solidity")[1].split("```")[0]
                with open("exploit.t.sol", "w") as f:
                    f.write(exploit_code)
                print("\n--- PRACTICAL EXPLOIT GENERATED: exploit.t.sol ---")
                
            return 
            
        except Exception as e:
            if "429" in str(e):
                wait_time = (attempt + 1) * 30
                print(f"Quota full. Waiting {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise e

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    args = parser.parse_args()
    run_audit(args.path)