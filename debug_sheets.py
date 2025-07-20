import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate with Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Print all accessible sheet names
sheets = client.openall()
for sheet in sheets:
    print(sheet.title)
