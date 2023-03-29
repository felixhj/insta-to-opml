import csv

# Define the HTML expression with placeholders for the values
html_template = "<div><p>Name: {name}</p></div>"

# Open the CSV file and read the data
with open('/Users/lucytiffen/pythonscripts/usernames_short.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Insert the values into the HTML expression and print the result
        html = html_template.format(name=row[0])
        outfile.write(html)
