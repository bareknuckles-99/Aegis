require('dotenv').config();
const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors()); // Allows your HTML to talk to this server

// sending pat token to the dashboard >> safe
app.get('/config', (req, res) => {
    res.json({
        github_pat: process.env.GITHUB_PAT,
        username: "bareknuckles-99"
    });
});

app.listen(3000, () => console.log('Aegis Bridge running on http://localhost:3000'));