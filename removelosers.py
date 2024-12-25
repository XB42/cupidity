import csv
from datetime import datetime

def calculate_age(birthdate):
    print(birthdate)
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

def filter_profiles(input_file, output_file):
    filtered_profiles = []

    with open(input_file, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='»')
        for row in reader:
            if row["Gender"] == "Female":
                continue
            if row["Date of birth"] == "n":
                continue
            age = calculate_age(row["Date of birth"])
            if (
                age >= 18 and
                row["What is your current relationship status?"] == "Single" and
                row["Are you open to meeting someone outside your preferences, in case we were not able to find a suitable date?"] == "Yes"
            ):
                row["Age"] = age  # Add age to the row for reference
                filtered_profiles.append(row)

    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = list(filtered_profiles[0].keys()) if filtered_profiles else []
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='»')
        writer.writeheader()
        writer.writerows(filtered_profiles)
