{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ef0f48a9-fa23-4e04-b999-68189f3cd5b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Comments written to file successfully.\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import json\n",
    "\n",
    "# Function to get comments for a specific email address\n",
    "def get_comments(email):\n",
    "    url = f\"https://jsonplaceholder.typicode.com/comments?email={email}\"\n",
    "    response = requests.get(url)\n",
    "    if response.status_code == 200:\n",
    "        return response.json()\n",
    "    else:\n",
    "        print(f\"Failed to fetch comments for {email}\")\n",
    "        return []\n",
    "\n",
    "# Function to write comments to a file\n",
    "def write_comments_to_file(comments):\n",
    "    with open(\"comments.txt\", \"w\") as file:\n",
    "        for comment in comments:\n",
    "            name = extract_first_name(comment['email'])\n",
    "            body = comment['body']\n",
    "            file.write(f\"{name}: {body}\\n\\n\")\n",
    "\n",
    "# Function to extract the first name from an email address\n",
    "def extract_first_name(email):\n",
    "    special_characters = ['@', '.', '_', '-']\n",
    "    for char in email:\n",
    "        if char in special_characters:\n",
    "            return email[:email.index(char)]\n",
    "    return email  # If no special character found, return the full email\n",
    "\n",
    "# List of email addresses\n",
    "emails = [\"Jackeline@eva.tv\", \"Madaline@marlin.org\", \"Hermann.Kunde@rosina.us\"]\n",
    "\n",
    "# Dictionary to store comments for each user\n",
    "comments_dict = {}\n",
    "\n",
    "# Fetch comments for each user\n",
    "for email in emails:\n",
    "    comments_dict[email] = get_comments(email)\n",
    "\n",
    "# Write comments to file\n",
    "write_comments_to_file(comments_dict[\"Jackeline@eva.tv\"] + comments_dict[\"Madaline@marlin.org\"] + comments_dict[\"Hermann.Kunde@rosina.us\"])\n",
    "\n",
    "print(\"Comments written to file successfully.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5da6c73b-1469-4299-a3ca-2339f0e68adf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
