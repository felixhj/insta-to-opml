import pandas as pd
from tkinter import Tk, filedialog
from getch import getch
import csv

# choose input file
root = Tk()
root.withdraw()
input_file_path = filedialog.askopenfilename(title="Select input file", filetypes=[("CSV Files", "*.csv")])
if not input_file_path:
    print("No input file selected. Exiting...")
    exit()

# linebreaker
# Open the CSV file for reading
# with open(input_file_path, 'r') as file:
# csv_reader = csv.reader(file)
# 
#     # Open the same CSV file for writing
#     with open('new_data.csv', 'w', newline='') as new_file:
#         csv_writer = csv.writer(new_file)
# 
#         # Iterate over each row in the CSV file
#         for row in csv_reader:
# 
#             # Iterate over each value in the row
#             for value in row:
# 
#                 # Write each value as a new row in the new CSV file
#                 csv_writer.writerow([value])
# 
# # open the input and output CSV files
# with open('new_data.csv', newline='') as input_file, \
#      open('new_data2.csv', 'w', newline='') as output_file:
#      
#     reader = csv.reader(input_file)
#     writer = csv.writer(output_file)
#     
#     # iterate over each row in the input CSV file
#     for row in reader:
#         # remove spaces from the beginning of each row
#         updated_row = [cell.lstrip() for cell in row]
#         
#         # write the updated row to the output CSV file
#         writer.writerow(updated_row)
# 
# input_file_path = "~/new_data2.csv"

print (input_file_path)
# choose number of groups
num_groups = int(input("Enter number of groups: "))

# choose group names
group_names = []
for i in range(num_groups):
    group_names.append(input(f"Enter name for group {i+1}: "))

# load data from input file
data = pd.read_csv(input_file_path)

# loop through each value in data and ask user to categorize it into one of the groups
current_index = 0
while current_index < len(data):
    value = data.iloc[current_index, 0]
    print ("\n")
    print(f"Value: {value}")
    group = None
    while group is None:
        print("Choose a group number:")
        for i in range(num_groups):
            print(f"{i+1}: {group_names[i]}")
        key = ord(getch())
        if key in range(49, 49+num_groups):
            group = key - 48
            print(f"Group: {group_names[group-1]}")
    data.at[current_index, 'Group'] = group_names[group-1]
    current_index += 1

# save data to separate files for each group
for i in range(num_groups):
    group_data = data[data['Group'] == group_names[i]]
    group_file_path = input_file_path.replace(".csv", f"_{group_names[i]}.csv")
    group_data.to_csv(group_file_path, index=False)
    
    
for i in range(num_groups):    
	# Load the CSV file into a DataFrame
	df = pd.read_csv(group_file_path, header=None)

	# Drop the second column (index=1) and save the result in the same DataFrame
	df.drop(df.columns[1], axis=1, inplace=True)

	# Save the modified DataFrame to a new CSV file
	df.to_csv(group_file_path, header=None, index=None)
