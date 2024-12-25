import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
import os


def fetch_google_sheet_data_to_csv(json_keyfile, sheet_key="1Ob6IIKJPdklsKsaPtQGM88OoNpyPMYi3KAVFqBJ7ce0"):
    """
    Fetches all data from the specified Google Sheet and saves it as a CSV file with '&&%' as the delimiter
    in the same folder as the script.

    Args:
        json_keyfile (str): Path to the JSON keyfile for Google API authentication.
        sheet_key (str): The key (ID) of the Google Sheet to fetch data from.

    Returns:
        str: Path to the created CSV file.
    """
    # Define scope and authenticate
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, scope)
    client = gspread.authorize(credentials)

    # Open Google Sheet by key and get the first sheet
    sheet = client.open_by_key(sheet_key).sheet1

    # Fetch all data from the sheet
    data = sheet.get_all_records()

    # Define output CSV file name in the same folder as the script
    output_csv = os.path.join(os.getcwd(), 'output.csv')

    # Save data to a CSV file with '&&%' as the delimiter
    with open(output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
        if data:
            writer = csv.DictWriter(csv_file, fieldnames=data[0].keys(), delimiter='»')
            writer.writeheader()
            writer.writerows(data)
