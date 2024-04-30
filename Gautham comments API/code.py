
import requests
import json

# Function to get comments for a specific email address
def get_comments(email):
    url = f"https://jsonplaceholder.typicode.com/comments?email={email}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch comments for {email}")
        return []

# Function to write comments to a file
def write_comments_to_file(comments):
    with open("comments.txt", "w") as file:
        for comment in comments:
            name = extract_first_name(comment['email'])
            body = comment['body']
            file.write(f"{name}: {body}\n\n")

# Function to extract the first name from an email address
def extract_first_name(email):
    special_characters = ['@', '.', '_', '-']
    for char in email:
        if char in special_characters:
            return email[:email.index(char)]
    return email  # If no special character found, return the full email

# List of email addresses
emails = ["Jackeline@eva.tv", "Madaline@marlin.org", "Hermann.Kunde@rosina.us"]

# Dictionary to store comments for each user
comments_dict = {}

# Fetch comments for each user
for email in emails:
    comments_dict[email] = get_comments(email)

# Write comments to file
write_comments_to_file(comments_dict["Jackeline@eva.tv"] + comments_dict["Madaline@marlin.org"] + comments_dict["Hermann.Kunde@rosina.us"])

print("Comments written to file successfully.")
