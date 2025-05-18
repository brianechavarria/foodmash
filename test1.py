from google.ouath2 import service_account
from googapiclient.discovery import build

SERVICE_ACCOUNT_FILE = 'glossy-beach-456620-s8-9f8aa8d160d4.json'
credentials = service_account.Credentials.from_service_account_file(
    filename=SERVICE_ACCOUNT_FILE
)

service_sheets = build('sheets', 'v4', credentials=credentials)
print(service_sheets)