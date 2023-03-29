import instaloader
import csv

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