from sheetreader import fetch_google_sheet_data_to_csv
from sheetcleaner import remove_first_duplicates
from gendersplitter import split_csv_by_gender
from compatibilities import save_scores_to_csv
from removelosers import filter_profiles
from couplescorer import calculate_couple_scores
from resultuploader import copy_csv_to_google_sheet
from finaloutputter import merge_and_sort_csv

# Example usage:
if __name__ == "__main__":
    json_keyfile = 'credentials.json'  # Path to your credentials JSON file
    sheet_key = "1Ob6IIKJPdklsKsaPtQGM88OoNpyPMYi3KAVFqBJ7ce0"  # Replace with your Google Sheet key
    
fetch_google_sheet_data_to_csv(json_keyfile, sheet_key)
remove_first_duplicates(
    input_file='output.csv',
    output_file='output_file_cleaned.csv'
)

# Usage
input_csv = 'output_file_cleaned.csv'  # Input CSV file name
output_csv = 'filtered_male_profiles.csv'  # Output CSV file name
filter_profiles(input_csv, output_csv)

split_csv_by_gender('output_file_cleaned.csv')



save_scores_to_csv('male.csv', 'female.csv', 'thesislist.json', 'outputscores.csv')
calculate_couple_scores('criteriaweight.json', 'outputscores.csv', 'compatibilityscores.csv')

merge_and_sort_csv(
    'compatibilityscores.csv',
    'output_file_cleaned.csv',
    'final.csv'
)

copy_csv_to_google_sheet(
    service_account_file='credentials.json',
    sheet_id='1Ob6IIKJPdklsKsaPtQGM88OoNpyPMYi3KAVFqBJ7ce0',
    worksheet_name='scores',
    csv_file='final.csv'
)
