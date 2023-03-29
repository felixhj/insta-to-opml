import instaloader
import csv
import pandas as pd
from tkinter import Tk, filedialog
from getch import getch
from lxml import etree

# Instagram URL format
insta="https://www.instagram.com/"

for i in range(num_groups):
	# Read URLs from CSV file
	urls = []
	with open(f"./following_{group_names[i]}.csv", 'r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			urls.append(row[0])

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
	with open(f"{group_names[i]}.opml", "wb") as f:
		f.write(etree.tostring(opml, pretty_print=True))