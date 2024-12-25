import csv

def remove_first_duplicates(input_file, output_file):
    # Read the CSV file with the custom delimiter
    with open(input_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\u00bb')
        rows = list(reader)

    seen_emails = set()
    cleaned_rows = []

    for row in rows:
        email = row.get("Email")
        if email in seen_emails:
            # Keep duplicate entries but skip the first occurrence
            continue
        else:
            seen_emails.add(email)
            cleaned_rows.append(row)

    # Write back the cleaned data
         # Write back the cleaned data
    with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames, delimiter='\u00bb')
        writer.writeheader()
        writer.writerows(cleaned_rows)
