import csv
import json

# Define the input CSV file and output JSON file paths
csv_file_path = 'board.csv'
json_file_path = 'board.json'

# Initialize a dictionary to hold the categorized data
categorized_data = {
    'Board/Management': [],
    'Board/Marketing': [],
    'Board/Design': [],
    'Board/Chair': [],
    'Board/Executive': []
}

# Function to ensure LinkedIn URLs are valid
def ensure_linkedin_url(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        return 'https://' + url
    return url

# Open and read the CSV file
with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        vertical = row['vertical']
        # Check if the vertical matches one of the categories
        if vertical in categorized_data:
            # Append the row to the appropriate category in categorized_data
            categorized_data[vertical].append({
                'id': row['id'],
                'name': row['name'],
                'position': row['position'],
                'imgSrc': row['imgSrc'],
                'LinkedIn': ensure_linkedin_url(row['LinkedIn']),
                'FavProduct': row['FavProduct'],
                'WhyPS': row['WhyPS']
            })

# Write the categorized data to a JSON file
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(categorized_data, jsonfile, indent=4)

print("Board CSV data has been successfully categorized and saved to JSON.")
