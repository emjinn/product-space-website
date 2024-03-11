import csv
import json

# Define the input CSV file and output JSON file paths
csv_file_path = 'members.csv'
json_file_path = 'members.json'

# Initialize a dictionary to hold the categorized data
categorized_data = {
    'Design Fellow': [],
    'Marketing Fellow': [],
    'Management Fellow': []
}

# Open and read the CSV file
with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        position = row['position']
        # Check if the position matches one of the categories
        if position in categorized_data:
            # Append the row to the appropriate category in categorized_data
            categorized_data[position].append({
                'id': row['id'],
                'name': row['name'],
                'position': row['position'],
                'imgSrc': row['imgSrc'],
                'LinkedIn': row['LinkedIn'],
                'FavProduct': row['FavProduct'],
                'WhyPS': row['WhyPS']
            })

# Write the categorized data to a JSON file
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(categorized_data, jsonfile, indent=4)

print("CSV data has been successfully categorized and saved to JSON.")


