import csv

# opening HTML file
Func = open("output.html","w")
   
# Adding input data to the HTML file
Func.write("<?xml version=" '"1.0"' "encoding=" '"UTF-8"' "?>\n<opml version=" '"1.0"' ">\n<head>\n<title>Feed Subscriptions</title>\n</head>\n<body>\n")
              
# Saving the data into the HTML file
Func.close()


# Define the HTML expression with placeholders for the values
html_template = "      <outline type=" '"rss"' "\n            " "htmlUrl=" '"https://www.instagram.com/{name}/"' " xmlUrl=" '"https://www.instagram.com/{name}/"' "/> \n"

# Open the CSV file and read the data
with open('/Users/lucytiffen/pythonscripts/usernames_short.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    # Create a new file to write the HTML output
    with open('output.html', 'a') as outfile:
        # Loop through the rows and generate the HTML for each row
        for row in reader:
            # Insert the values into the HTML expression
            name = row[0]
            html = html_template.format(name=name)
            # Write the HTML for this row to the output file
            outfile.write(html)

# opening HTML file
Func = open("output.html","a")
   
# Adding input data to the HTML file
Func.write("\t</outline>\n</body>\n</opml>")
              
# Saving the data into the HTML file
Func.close()

# Exit
exit() 