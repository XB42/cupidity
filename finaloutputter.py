import csv

def merge_and_sort_csv(csv1_path, csv2_path, output_path):
    # Read csv1 into lists
    with open(csv1_path, 'r', encoding='utf-8') as file1:
        reader1 = csv.reader(file1)
        categories1 = next(reader1)
        data_dict1 = {category: [] for category in categories1}
        for row in reader1:
            for index, value in enumerate(row):
                data_dict1[categories1[index]].append(value)

    # Read csv2 into lists using '»' as a delimiter
    with open(csv2_path, 'r', encoding='utf-8') as file2:
        reader2 = csv.reader(file2, delimiter='»')
        categories2 = next(reader2)
        data_dict2 = {category: [] for category in categories2}
        for row in reader2:
            for index, value in enumerate(row):
                data_dict2[categories2[index]].append(value)

    # Sort data1 by the 'Total' column in descending order
    sorted_indices = sorted(range(len(data_dict1['Total'])), key=lambda i: float(data_dict1['Total'][i]), reverse=True)
    sorted_data1 = {key: [data_dict1[key][i] for i in sorted_indices] for key in data_dict1}
    merged_data_final = []
    merged_data_final.append(["Man name", "Woman Name", "Man Email", "Woman Email", "Man Phone", "Woman Phone", "Score"])  
    for i in range(len(sorted_data1['Total'])):
        # Merge sorted_data1 with the corresponding details from data2
        merged_data = []
        memail = sorted_data1['Male'][i]
        femail = sorted_data1['Female'][i]

        mid = data_dict2['Email'].index(memail)
        fid = data_dict2['Email'].index(femail)

        for category in categories2:
            if category == 'Email' or category == "Phone number (WhatsApp compatible)" or category == "Full Name":
                merged_data.append(data_dict2[category][mid])
                merged_data.append(data_dict2[category][fid])

        merged_data.append(sorted_data1['Total'][i])
        print(sorted_data1['Total'][i])
        merged_data_final.append(merged_data)
        merged_data = []


    with open(output_path, 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)

    # If the first sub-list is meant to be headers, you could write that row separately:
    # writer.writerow(merged_data[0])
    # for row in merged_data[1:]:
    #     writer.writerow(row)

    # Or simply write all rows in one go:
        for row in merged_data_final:
            writer.writerow(row)
    



    print(f"Merged and sorted CSV saved to {output_path}")

# Example usage:
# merge_and_sort_csv('csv1.csv', 'csv2.csv', 'output.csv')
