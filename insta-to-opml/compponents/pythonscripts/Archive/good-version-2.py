import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Function to allow user to select input file
def get_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

# Function to allow user to select number of groups and their names
def get_groups():
    num_groups = int(input("Enter number of groups: "))
    group_names = []
    for i in range(num_groups):
        name = input("Enter name of group {}: ".format(i+1))
        group_names.append(name)
    return num_groups, group_names

# Function to categorize values into groups
def group_values():
    # Get input file and number/groups names
    file_path = get_file()
    num_groups, group_names = get_groups()
    
    # Load data into pandas DataFrame
    df = pd.read_csv(file_path, header=None)
    
    # Create dictionary to hold data for each group
    groups = {}
    for name in group_names:
        groups[name] = []
        
    # Iterate through data and allow user to categorize each value
    print("\nPress the number key corresponding to the group you want to categorize the value into.")
    for index, row in df.iterrows():
        value = row[0]
        print (group_names)
        print("\n {}".format(value))
        group = input()
        while not group.isdigit() or int(group) < 1 or int(group) > num_groups:
            print("Invalid input. Please enter a number between 1 and {}.".format(num_groups))
            group = input()
        group_name = group_names[int(group)-1]
        groups[group_name].append(value)
    
    # Save categorized data to new csv files
    for name, data in groups.items():
        df = pd.DataFrame(data)
        df.to_csv("{}_{}.csv".format(file_path[:-4], name), index=False, header=False)
    print("\nData has been categorized and saved to new csv files.")

# Call the function to categorize values
group_values()
