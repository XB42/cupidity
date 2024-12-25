import csv

def split_csv_by_gender(input_file):
    male_file = "male.csv"
    female_file = "female.csv"

    # Columns to remove
    columns_to_remove = [
        "Please upload your photo",
        "Preferred height of partner (optional)",
        "I have read and understood this point",
        "Are you open to meeting someone outside your preferences, in case we were not able to find a suitable date?",
        "Phone number (WhatsApp compatible)",
        "Full Name",
        "Submission time",
        "Submission ID",
        "Gender",
        "Is there anything else you would like us to know or consider when making a match?",
        "Your height"
    ]

    try:
        with open(input_file, mode='r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile, delimiter='»')

            # Ensure the Gender column exists
            if 'Gender' not in reader.fieldnames:
                raise ValueError("The input file does not contain a 'Gender' column.")

            # Filter out unwanted columns and columns with empty headers
            filtered_fieldnames = [
                col for col in reader.fieldnames 
                if col not in columns_to_remove and col.strip()
            ]

            # Open output files
            with open(male_file, mode='w', encoding='utf-8', newline='') as male_out, \
                 open(female_file, mode='w', encoding='utf-8', newline='') as female_out:

                male_writer = csv.DictWriter(male_out, fieldnames=filtered_fieldnames, delimiter='»')
                female_writer = csv.DictWriter(female_out, fieldnames=filtered_fieldnames, delimiter='»')

                # Write headers
                male_writer.writeheader()
                female_writer.writeheader()

                # Write rows to corresponding files
                for row in reader:
                    # Remove unwanted columns
                    filtered_row = {key: value if value else ":empty:" for key, value in row.items() if key in filtered_fieldnames}

                    if row['Gender'].strip().lower() == 'male':
                        male_writer.writerow(filtered_row)
                    elif row['Gender'].strip().lower() == 'female':
                        female_writer.writerow(filtered_row)

        print(f"Files created successfully: {male_file}, {female_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
