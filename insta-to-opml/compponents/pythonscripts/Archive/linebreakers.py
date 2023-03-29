from tkinter import Tk, filedialog
import csv


# choose input file
root = Tk()
root.withdraw()
input_file_path = filedialog.askopenfilename(title="Select input file", filetypes=[("CSV Files", "*.csv")])
if not input_file_path:
    print("No input file selected. Exiting...")
    exit()

# Open the CSV file for reading
with open(input_file_path, 'r') as file:
    csv_reader = csv.reader(file)

    # Open the same CSV file for writing
    with open('new_data.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file)

        # Iterate over each row in the CSV file
        for row in csv_reader:

            # Iterate over each value in the row
            for value in row:

                # Write each value as a new row in the new CSV file
                csv_writer.writerow([value])

# open the input and output CSV files
with open('new_data.csv', newline='') as input_file, \
     open('new_data2.csv', 'w', newline='') as output_file:
     
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    
    # iterate over each row in the input CSV file
    for row in reader:
        # remove spaces from the beginning of each row
        updated_row = [cell.lstrip() for cell in row]
        
        # write the updated row to the output CSV file
        writer.writerow(updated_row)