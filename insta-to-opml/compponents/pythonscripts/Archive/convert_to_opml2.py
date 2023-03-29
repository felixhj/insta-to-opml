import csv

# Specify the file paths of the input and output CSV files
input_csv_file_path = "/Users/lucytiffen/pythonscripts/usernames_short.csv"
output_csv_file_path = "output.csv"

# Define the text to add to each row in the input CSV file
text_to_add = 

add_before_value = True  # Set to True to add text before the value, or False to add text after the value

# Open the input CSV file in read mode and the output CSV file in write mode
with open(input_csv_file_path, "r", newline="") as input_csv_file, open(output_csv_file_path, "w", newline="") as output_csv_file:
    # Create a CSV reader object for the input CSV file
    reader = csv.reader(input_csv_file)

    # Create a CSV writer object for the output CSV file
    writer = csv.writer(output_csv_file)

    # Check if the input CSV file has a header row
    has_header = csv.Sniffer().has_header(input_csv_file.read(1024))
    input_csv_file.seek(0)  # Reset the file pointer to the beginning of the file

    # Loop over each row in the input CSV file
    for row in reader:
        # Get the original value from the row
        original_value = row[0]

        # Add the text before or after the value
        if add_before_value:
            updated_value = text_to_add + original_value
        else:
            updated_value = original_value + text_to_add

        # Update the row with the new value
        row[0] = updated_value

        # Write the updated row to the output CSV file
        writer.writerow(row)
