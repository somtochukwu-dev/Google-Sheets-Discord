import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import time
import os  # Added for environment variables

# Google Sheets auth setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Your Sheet Name Here").sheet1  # Replace with your sheet title

# Discord webhook URL (use an environment variable for safety)
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

if not WEBHOOK_URL:
    raise ValueError("❌ DISCORD_WEBHOOK_URL environment variable not set")

# Track row count
existing_rows = len(sheet.get_all_values())
print(f"✅ Bot is live. Watching for new rows... (Current rows: {existing_rows})")

while True:
    current_values = sheet.get_all_values()
    new_count = len(current_values)

    if new_count > existing_rows:
        headers = current_values[0]
        new_row = current_values[-1]
        new_data = dict(zip(headers, new_row))

        # Formatted premium message
        message = (
            f"📋 **New Task Logged**\n\n"
            f"👤 **Name:** {new_data.get('Name')}\n"
            f"✉️ **Email:** {new_data.get('Email')}\n"
            f"📝 **Task:** {new_data.get('Task')}\n"
            f"✅ **Status:** {new_data.get('Status')}\n"
            f"⚡ **Priority:** {new_data.get('Priority')}"
        )

        # Send to Discord
        response = requests.post(WEBHOOK_URL, json={"content": message})
        print(f"✅ Posted: {new_data['Name']} | Row {new_count} | Status: {response.status_code}")

        existing_rows = new_count

    time.sleep(10)
