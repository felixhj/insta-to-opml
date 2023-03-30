# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# (echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/lucytiffen/.zprofile
#	  eval "$(/opt/homebrew/bin/brew shellenv)"
# brew install python

import sys
import subprocess

# Check if pip is installed
result = subprocess.run(['which', 'pip'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if result.returncode == 0:
    pip_cmd = 'pip'
else:
    # Check if pip3 is installed
    result = subprocess.run(['which', 'pip3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        pip_cmd = 'pip3'
    else:
        print("Error: pip or pip3 is not installed")
        exit(1)

# Use pip_cmd to run pip commands
result = subprocess.run([pip_cmd, '--version'])

# List of dependencies to install
dependencies = ['pandas','tk','getch','lxml','argparse','wheel']

# Loop through each dependency and install it
for dep in dependencies:
	subprocess.check_call([pip_cmd, 'install', dep])

import instaloader
import csv
import pandas as pd
import os
from tkinter import filedialog, Tk
from getch import getch
from lxml import etree
from argparse import ArgumentParser
from glob import glob
from os.path import expanduser
from platform import system
from sqlite3 import OperationalError, connect

try:
	from instaloader import ConnectionException, Instaloader
except ModuleNotFoundError:
	raise SystemExit("Instaloader not found.\n	pip install [--user] instaloader")

## SELECT FIREFOX PROFILE
 
root = Tk()
root.withdraw() # hide the root window
ff_dir_path = filedialog.askdirectory(initialdir = os.path.expanduser("~/Library/Application Support/Firefox/Profiles"), title = "Select profile folder")
print (ff_dir_path)
def get_cookiefile():
	default_cookiefile = {
		"Windows": "~/AppData/Roaming/Mozilla/Firefox/Profiles/*/cookies.sqlite",
		"Darwin": f"{ff_dir_path}/cookies.sqlite",
	}.get(system(), "~/.mozilla/firefox/*/cookies.sqlite")
	cookiefiles = glob(expanduser(default_cookiefile))
	if not cookiefiles:
		raise SystemExit("No Firefox cookies.sqlite file found. Use -c COOKIEFILE.")
	return cookiefiles[0]


def import_session(cookiefile, sessionfile):
	print("Using cookies from {}.".format(cookiefile))
	conn = connect(f"file:{cookiefile}?immutable=1", uri=True)
	try:
		cookie_data = conn.execute(
			"SELECT name, value FROM moz_cookies WHERE baseDomain='instagram.com'"
		)
	except OperationalError:
		cookie_data = conn.execute(
			"SELECT name, value FROM moz_cookies WHERE host LIKE '%instagram.com'"
		)
	instaloader = Instaloader(max_connection_attempts=1)
	instaloader.context._session.cookies.update(cookie_data)
	username = instaloader.test_login()
	if not username:
		raise SystemExit("Not logged in. Are you logged in successfully in Firefox?")
	print("Imported session cookie for {}.".format(username))
	instaloader.context.username = username
	instaloader.save_session_to_file(sessionfile)


if __name__ == "__main__":
	p = ArgumentParser()
	p.add_argument("-c", "--cookiefile")
	p.add_argument("-f", "--sessionfile")
	args = p.parse_args()
	try:
		import_session(args.cookiefile or get_cookiefile(), args.sessionfile)
	except (ConnectionException, OperationalError) as e:
		raise SystemExit("Cookie import failed: {}".format(e))

# Create an instance of Instaloader class
L = instaloader.Instaloader()

# Login to Instagram account
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")
L.context.log("Logging in...")
L.load_session_from_file(username)
if not L.context.is_logged_in:
	L.context.log("Login failed!")
	exit()

# Get the profile of the logged in user
profile = instaloader.Profile.from_username(L.context, username)

# Get the list of profiles followed by the logged in user
following = set(profile.get_followees())

# Write the usernames to a .csv file
with open('following.csv', mode='w', newline='') as file:
	writer = csv.writer(file)
	for followee in following:
		writer.writerow([followee.username])

###############################

# # newline for every value, remove whitespace
# Open the CSV file for reading
# with open(input_file_path, 'r') as file:
# csv_reader = csv.reader(file)
# 
#	  # Open the same CSV file for writing
#	  with open('new_data.csv', 'w', newline='') as new_file:
#		  csv_writer = csv.writer(new_file)
# 
#		  # Iterate over each row in the CSV file
#		  for row in csv_reader:
# 
#			  # Iterate over each value in the row
#			  for value in row:
# 
#				  # Write each value as a new row in the new CSV file
#				  csv_writer.writerow([value])
# 
# # open the input and output CSV files
# with open('new_data.csv', newline='') as input_file, \
#	   open('new_data2.csv', 'w', newline='') as output_file:
#	   
#	  reader = csv.reader(input_file)
#	  writer = csv.writer(output_file)
#	  
#	  # iterate over each row in the input CSV file
#	  for row in reader:
#		  # remove spaces from the beginning of each row
#		  updated_row = [cell.lstrip() for cell in row]
#		  
#		  # write the updated row to the output CSV file
#		  writer.writerow(updated_row)
# 
# input_file_path = "~/new_data2.csv"

# Prompt the user to split into groups
response = input("Do you want to split into groups? (y/n): ")

# Check the user's response
if response.lower() == "y":
	# Execute code block x if the user wants to split into groups
	print("Code block x: Splitting into groups...")
	# Add your code block x here
	# choose number of groups
	num_groups = int(input("Enter number of groups: "))

	# choose group names
	group_names = []
	for i in range(num_groups):
		group_names.append(input(f"Enter name for group {i+1}: "))

	# load data from input file
	data = pd.read_csv("following.csv", header=None)

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

	# save data to separate files for each group, only the first column, not including grouping data
	for i in range(num_groups):
		group_data = data[data['Group'] == group_names[i]].iloc[:,0]
		group_file_path = "following.csv".replace(".csv", f"_{group_names[i]}.csv")
		group_data.to_csv(group_file_path, index=False, header=None)

	## CONVERT CSV TO OPML
	# Instagram URL format
	insta="https://www.instagram.com/"

	for i in range(num_groups):
		# Read URLs from CSV file
		urls = []
		with open(f"following_{group_names[i]}.csv", 'r') as csvfile:
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
		folder = etree.SubElement(body, "outline", text=f"{group_names[i]}")

		# Convert each URL to an OPML outline
		for url in urls:
			outline = etree.SubElement(folder, "outline", text=url, title=url, type="rss", xmlUrl=insta+url)

		# Write the OPML file
		with open(f"{group_names[i]}.opml", "wb") as f:
			f.write(etree.tostring(opml, pretty_print=True))
		
		## DELETE CSV FILES	
		# specify the path of the file to delete
		file_path = f"following_{group_names[i]}.csv"

		# delete the file using the os.remove() method
		os.remove(file_path)
		
else:
	# Execute code block y if the user doesn't want to split into groups
	print("Code block y: Not splitting into groups...")
	# Add your code block y here

	# Instagram URL format
	insta="https://www.instagram.com/"

	# Read URLs from CSV file
	urls = []
	with open("following.csv", 'r') as csvfile:
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
	folder = etree.SubElement(body, "outline", text="following")

	# Convert each URL to an OPML outline
	for url in urls:
		outline = etree.SubElement(folder, "outline", text=url, title=url, type="rss", xmlUrl=insta+url)

	# Write the OPML file
	with open("following.opml", "wb") as f:
		f.write(etree.tostring(opml, pretty_print=True))
	
	## DELETE CSV FILES	
	# specify the path of the file to delete
	file_path = "following.csv"

	# delete the file using the os.remove() method
	os.remove(file_path)


