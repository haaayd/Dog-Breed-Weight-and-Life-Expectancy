import requests
from bs4 import BeautifulSoup

url = "https://dog-weight.com/breed-directory/"

response = requests.get(url) 
print(response.status_code)  # Check if the request was successful

soup = BeautifulSoup(response.text, "html.parser")
print(soup.title)