import requests
import os

# Discord webhook URL from environment variable
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

if not WEBHOOK_URL:
    raise ValueError("❌ DISCORD_WEBHOOK_URL environment variable not set")

# Message payload
data = {
    "content": "✅ GoStreamlined Bot test successful! Automation works perfectly."
}

# Send POST request to Discord
response = requests.post(WEBHOOK_URL, json=data)

# Optional: print the status
if response.status_code == 204:
    print("Message sent successfully to Discord!")
else:
    print(f"Failed to send message: {response.status_code}")
