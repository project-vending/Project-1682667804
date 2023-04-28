python
import os
import json

input_file = 'data/raw/data.json'
output_file = 'data/transformed/transformed_data.json'

if os.path.exists(input_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Apply your data transformations here
    transformed_data = []

    for item in data:
        new_item = {}
        new_item['id'] = item['id']
        new_item['name'] = item['name'].upper()
        new_item['age'] = item['age'] + 5
        transformed_data.append(new_item)

    # Write transformed data to the output file
    with open(output_file, 'w') as f:
        json.dump(transformed_data, f)

    print(f"Data transformed successfully and saved in {output_file}!")
else:
    print(f"No input file found at {input_file}. Please make sure you've added the data file in the correct location.")
