import csv
from lxml import etree
from tkinter import Tk, filedialog

#select file name
file_name = input("Please enter a file name: ")
print("The file name you entered is:", file_name)

# opening HTML file
Func = open(f"{file_name}.html","w")
   
# Adding input data to the HTML file
Func.write("<?xml version=" '"1.0"' "encoding=" '"UTF-8"' "?>\n<opml version=" '"1.0"' ">\n<head>\n<title>Feed Subscriptions</title>\n</head>\n<body>\n")
              
# Saving the data into the HTML file
Func.close()


# Define the HTML expression with placeholders for the values
html_template = "      <outline type=" '"rss"' "\n            " "xmlUrl=" '"https://www.instagram.com/{name}/" ' "htmlUrl=" '"https://www.instagram.com/{name}/"' "/> \n"

# choose input file
root = Tk()
root.withdraw()
csv_input_file_path = filedialog.askopenfilename(title="Select input file", filetypes=[("CSV Files", "*.csv")])
if not csv_input_file_path:
    print("No input file selected. Exiting...")
    exit()

# Open the CSV file and read the data
with open(csv_input_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    # Create a new file to write the HTML output
    with open(f"{file_name}.html", 'a') as outfile:
        # Loop through the rows and generate the HTML for each row
        for row in reader:
            # Insert the values into the HTML expression
            name = row[0]
            html = html_template.format(name=name)
            # Write the HTML for this row to the output file
            outfile.write(html)
			# Check if this is the last row
            try:
                next(reader)
            except StopIteration:
                break

# opening HTML file
Func = open(f"{file_name}.html",'a')
   
# Adding input data to the HTML file
Func.write("\t</outline>\n</body>\n</opml>")
              
# Saving the data into the HTML file
Func.close()

# Parse the HTML file
with open(f"{file_name}.html", 'r') as infile:
    html = infile.read()
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Create the OPML document
opml = etree.Element('opml')
head = etree.SubElement(opml, 'head')
title = etree.SubElement(head, 'title')
title.text = 'Converted from HTML'
body = etree.SubElement(opml, 'body')

# Convert the HTML tree to an OPML outline
def convert_element(element):
    outline = etree.Element('outline', text=element.tag)
    for attr, value in element.attrib.items():
        if attr == 'href':
            outline.set('xmlUrl', value)
        else:
            outline.set(attr, value)
    for child in element:
        outline.append(convert_element(child))
    return outline

outline = convert_element(tree)
body.append(outline)

# Write the OPML document to a file
with open(f"{file_name}.opml", 'wb') as outfile:
    outfile.write(etree.tostring(opml, pretty_print=True))
