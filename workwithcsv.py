import csv

# Function to clean and capitalize name fields
def clean_and_capitalize_name(name):
    cleaned_name = name.strip()
    return cleaned_name.capitalize()

# Original CSV file path
csv_file_path = '/path/to/original/csv/file'

# Step 1: Read the original CSV file and print each record
print("Step 1: Original Records")
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# Step 2: Clean the data
print("\nStep 2: Cleaned Records")
cleaned_records = []
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        cleaned_row = [field.strip() for field in row]
        cleaned_row[0] = clean_and_capitalize_name(cleaned_row[0])
        cleaned_row[1] = clean_and_capitalize_name(cleaned_row[1])
        cleaned_records.append(cleaned_row)
        print(cleaned_row)

# Step 3: Write the cleaned records to a new CSV file
new_csv_file_path = '/path/to/new/csv/file'
with open(new_csv_file_path, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    for row in cleaned_records:
        csv_writer.writerow(row)

# Step 4: Add a new record
new_record = ['Adrain', 'Cover', '10/10/10', '42 Hole close', 'The Glenn', '2000', '$123']
new_record[0] = clean_and_capitalize_name(new_record[0])
new_record[1] = clean_and_capitalize_name(new_record[1])
new_record = [field.strip() for field in new_record]
with open(new_csv_file_path, 'a', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(new_record)

# Step 5: Read and display the updated CSV file
print("\nStep 5: Updated Records")
with open(new_csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    updated_records = [row for row in csv_reader]
    for row in updated_records:
        print(row)


   

