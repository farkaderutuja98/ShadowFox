import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://example.com"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract title
title = soup.title.text
print("Page Title:", title)

# Extract all links
for link in soup.find_all("a"):
    print(link.get("href"))