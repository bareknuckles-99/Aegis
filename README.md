# Aegis v1.0: Web3 Autonomous Cloud Auditor

Aegis is a serverless security reconnaissance tool designed to audit smart contract repositories directly in the cloud. By leveraging high-context AI and GitHub’s infrastructure, it identifies deep-logic vulnerabilities and generates structured reports without requiring a local development environment.

## Core Capabilities

* **Automated Reconnaissance**: Recursively crawls GitHub repositories to isolate and ingest core logic files such as .sol, .vy, and .rs.
* **High-Context Analysis**: Feeds the isolated codebase into the Gemini model to identify vulnerabilities that traditional static analyzers often miss.
* **Actionable Reporting**: Produces structured Markdown reports detailing bug severity, logic flaws, and reproducible code blocks.
* **Zero-Footprint Execution**: Operates entirely within GitHub Actions runners, eliminating the need for local dependencies or complex setups.

## Tech Stack

* **Interface**: HTML5/CSS3 Web Portal hosted via GitHub Pages.
* **Engine**: Python 3.10 Scripting.
* **Intelligence**: Google Gemini 2.0 Flash.
* **Orchestration**: GitHub Actions Workflows.

---

## How to Initialize

### 1. Fork and Configuration
Fork the repository and ensure your **GitHub Pages** setting is pointed to the **main** branch to host the frontend portal.

### 2. Environment Secrets
Add your AI API key to the repository to power the audit engine:
1. Navigate to **Settings > Secrets and variables > Actions**.
2. Add a secret named **GEMINI_API_KEY** with your Google AI Studio key.

### 3. Authorization
To trigger audits from the web portal, you must use a **GitHub Personal Access Token (PAT)** with **workflow** permissions.

---

## Usage

1. Open the live Aegis Web Portal.
2. Paste the URL of any public smart contract repository.
3. Click **INITIATE_SCAN** and provide your PAT when prompted.
4. Track live progress in the **Actions** tab of your GitHub repository.

---

## Disclaimer
This tool is developed for security research and educational purposes. Always obtain explicit permission before auditing third-party repositories.
