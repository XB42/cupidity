import csv
import gspread
from google.oauth2.service_account import Credentials

def copy_csv_to_google_sheet(service_account_file, sheet_id, worksheet_name, csv_file):
    """
    Copies data from a CSV file to a Google Sheet.

    Before uploading, the function deletes everything on the worksheet to ensure it’s empty.

    :param service_account_file: Path to the service account JSON file
    :param sheet_id: The ID of the Google Sheet
    :param worksheet_name: The name of the worksheet (tab) to write data into
    :param csv_file: Path to the input CSV file
    """
    # Authenticate with the Google Sheets API
    credentials = Credentials.from_service_account_file(
        service_account_file,
        scopes=[
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
    )

    gc = gspread.authorize(credentials)

    # Open the Google Sheet
    sheet = gc.open_by_key(sheet_id)
    worksheet = sheet.worksheet(worksheet_name)

    # Clear the worksheet before uploading new data
    worksheet.clear()

    # Read data from the CSV file
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        csv_data = list(csv_reader)

    # Write data to the Google Sheet
    worksheet.update('A1', csv_data)

    print("Data has been successfully copied to the Google Sheet.")
