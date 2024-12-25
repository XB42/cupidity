import csv
import itertools
import json
from paramscorer import calculate_thesis_score

# Load male and female data from CSV files
def load_csv_data(file_path, delimiter='»'):
    data = []
    with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=delimiter)
        for row in reader:
            data.append(row)
    return data

# Get a list of thesis categories from the thesis JSON
def get_thesis_categories(thesis_file):
    with open(thesis_file, "r") as f:
        thesis = json.load(f)
    return list(thesis.keys())

# Generate all pairs of males and females and calculate scores for each category
def generate_scores(male_data, female_data, thesis_file):
    categories = get_thesis_categories(thesis_file)
    scores = []
    male_full_list = load_csv_data(male_data)
    
    # Initialize a dictionary with categories as keys and empty lists as values
    data_dictm = {category: [] for category in categories}

    # Populate the dictionary
    for row in male_full_list:
        for index, value in enumerate(row):
            data_dictm[categories[index]].append(value)

    numberofm = len(data_dictm["Email"])

    female_full_list = load_csv_data(female_data)
    
    # Initialize a dictionary with categories as keys and empty lists as values
    data_dictf = {category: [] for category in categories}

    # Populate the dictionary
    for row in female_full_list:
        for index, value in enumerate(row):
            data_dictf[categories[index]].append(value)

    numberoff = len(data_dictf["Email"])

    scores=[]
     
    for i in range(numberofm):
        for j in range(numberoff):
            for category in categories:
                print (f"Calculating scores for category: {category}, {i}")
                result = calculate_thesis_score(data_dictm[category][j], data_dictf[category][i], category, thesis_file)
                scores.append([data_dictm["Email"][i], data_dictf["Email"][j], category, result.score])
    return scores

# Save scores to a CSV file
def save_scores_to_csv(male_data, female_data, thesis_file,output_file):
    scores = generate_scores(male_data, female_data, thesis_file)
    with open(output_file, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Male", "Female", "Category", "Score", "Explanation"])
        writer.writerows(scores)

