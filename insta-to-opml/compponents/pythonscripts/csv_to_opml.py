import csv
from lxml import etree
from tkinter import Tk, filedialog

#select file name
file_name = input("Please enter an output file name: ")
print("The file name you entered is:", file_name)

# choose input file
root = Tk()
root.withdraw()
csv_input_file_path = filedialog.askopenfilename(title="Select input file", filetypes=[("CSV Files", "*.csv")])
if not csv_input_file_path:
    print("No input file selected. Exiting...")
    exit()

# Read URLs from CSV file
urls = []
with open(csv_input_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        urls.append(row[0])

# Instagram URL format
insta="https://www.instagram.com/"

# Create a new OPML document
opml = etree.Element("opml", version="1.0")
head = etree.SubElement(opml, "head")
title = etree.SubElement(head, "title")
title.text = "My OPML"
body = etree.SubElement(opml, "body")

# Create a new folder for the URLs
folder = etree.SubElement(body, "outline", text="My URLs")

# Convert each URL to an OPML outline
for url in urls:
    outline = etree.SubElement(folder, "outline", text=url, title=url, type="rss", xmlUrl=insta+url)

# Write the OPML file
with open(f"{file_name}.opml", "wb") as f:
    f.write(etree.tostring(opml, pretty_print=True))
