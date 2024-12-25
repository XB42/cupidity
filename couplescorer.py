import csv
import json

def calculate_couple_scores(criteria_file, scores_file, output_file):
    # Load criteria weights from JSON file
    with open(criteria_file, 'r') as f:
        criteria_weights = json.load(f)

    # Load scores from CSV file
    with open(scores_file, 'r') as f:
        reader = csv.DictReader(f)
        scores = list(reader)

    # Calculate the total score for each couple
    def calculate_total_score(scores, criteria_weights):
        couples = {}
        for row in scores:
            male = row['Male']
            female = row['Female']
            category = row['Category']
            score = float(row['Score'])
            weight = criteria_weights.get(category, 0)
            total_score = score * weight

            # Combine scores for each couple
            key = (male, female)
            if key not in couples:
                couples[key] = 0
            couples[key] += total_score

        return couples

    # Process each unique pair and calculate their total score
    couples_scores = calculate_total_score(scores, criteria_weights)

    # Write the results to a new CSV file
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Male', 'Female', 'Total'])
        for (male, female), total in couples_scores.items():
            writer.writerow([male, female, total])

    print(f"Total scores calculated and saved to {output_file}")
