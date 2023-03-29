import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Function to get the file path using a file dialog
def get_file_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

# Function to get the number of groups and their names
def get_groups():
    num_groups = int(input("Enter the number of groups: "))
    group_names = []
    for i in range(num_groups):
        name = input(f"Enter the name of group {i+1}: ")
        group_names.append(name)
    return num_groups, group_names

# Function to categorize the values in the input CSV file into groups
def categorize_values(file_path, num_groups, group_names):
    df = pd.read_csv(file_path)
    num_rows = len(df.index)
    for i in range(num_rows):
        print(f"\nValue: {df.iloc[i, 0]}")
        while True:
            group = input("Enter the group number for the value (1, 2, or 3): ")
            if group in ['1', '2', '3']:
                group_num = int(group)
                df.loc[i, 'Group'] = group_names[group_num-1]
                break
            else:
                print("Invalid group number. Please enter 1, 2, or 3.")
    return df

# Function to save the categorized values to separate CSV files
def save_csv_files(df, group_names):
    for name in group_names:
        group_df = df.loc[df['Group'] == name]
        group_df.to_csv(f"{name}.csv", index=False)

# Main function to run the program
def main():
    file_path = get_file_path()
    num_groups, group_names = get_groups()
    categorized_df = categorize_values(file_path, num_groups, group_names)
    save_csv_files(categorized_df, group_names)

if __name__ == '__main__':
    main()
