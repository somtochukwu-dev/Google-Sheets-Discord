# 📊 Google Sheets ➝ Discord Automation

A Python automation bot that watches a Google Sheet for updates and posts new rows to a Discord channel using a webhook.

---

## 🚀 Features
- 📋 Watches Google Sheets in real-time.
- 🔗 Sends new data rows to a Discord channel.
- 🔒 Credentials and webhook kept secure via environment variables.

---

## 🗂 Project Structure
google-sheets-discord-bot/
├── credentials.json # Google API service account (placeholder)
├── debug_sheets.py # Lists all available sheets
├── sheets_to_discord.py # Watches for updates and posts to Discord
├── test_webhook.py # Test your Discord webhook
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/google-sheets-discord-bot.git
cd google-sheets-discord-bot
2️⃣ Install dependencies
bash
Copy code
pip install gspread oauth2client requests
3️⃣ Set up Google API credentials
Replace credentials.json with your own Google API service account credentials.

4️⃣ Set environment variable for Discord webhook
On Linux/Mac:

bash
Copy code
export DISCORD_WEBHOOK_URL="your-webhook-url"
On Windows:

cmd
Copy code
set DISCORD_WEBHOOK_URL=your-webhook-url
5️⃣ Run the bot
bash
Copy code
python sheets_to_discord.py
🔒 Security Notes
✅ Never upload real credentials or webhook URLs to GitHub.

✅ This repo uses placeholders for safety.

👨‍💻 Author
Developed by Somtochukwu O
