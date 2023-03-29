import csv
import pandas as pd

# Read in the CSV file
df = pd.read_csv('/Users/lucytiffen/pythonscripts/following_a.csv')

# Drop the second column
df = df.drop(df.columns[1], axis=1)

# Write the updated DataFrame back to the original CSV file
df.to_csv('/Users/lucytiffen/pythonscripts/following_a.csv', index=False)