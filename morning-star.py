import requests
from bs4 import BeautifulSoup

# Capterra
url = "https://www.capterra.com/categories/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# Extract the data you want from the HTML content
data = soup.find_all("div", class_="my-class")

# Store the data in a structured format
# For example, write the data to a CSV file
with open("capterra_data.csv", "w") as f:
    for item in data:
        f.write(item.text + "\n")