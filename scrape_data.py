import requests
from bs4 import BeautifulSoup

url = "https://dog-weight.com/breed-directory/"

response = requests.get(url) 
#print(response.status_code)  # Check if the request was successful

soup = BeautifulSoup(response.text, "html.parser")
#print(soup.title)

links = soup.find_all("a")

#print(len(links))

#for link in links:
#   print(link.get_text(strip=True), link.get("href"))

# Requesting the page for Border Collie
border_collie_url = "https://dog-weight.com/border-collie"

border_collie_response = requests.get(border_collie_url)

#print(border_collie_response.status_code)
border_collie_soup = BeautifulSoup(border_collie_response.text, "html.parser")
#print(border_collie_soup.title)
#print(border_collie_soup.get_text(" ", strip=True))

#locating Female Dogs element 
female_section = border_collie_soup.find(string="Female Dogs")
#print(female_section)

#print(female_section.parent)
#print(female_section.parent.parent)

# Finding all elements with "female" in their id attribute found ALL the elements saerch was to broad 
#female_elements = border_collie_soup.find_all(id=lambda x: x and "female" in x)

#for element in female_elements:
    #print(element)

female_weight = border_collie_soup.find(id="female-weight-value")
#print(female_weight) # we want to extract just the text from the element, not the entire tag
print(female_weight.get_text())

female_weight_text = female_weight.get_text()
print(female_weight_text)

female_weight_text = female_weight_text.replace(" lbs", "")
print(female_weight_text)

female_weight_numbers = female_weight_text.split(" - ")
print(female_weight_numbers)

female_weight_min = float(female_weight_numbers[0])
female_weight_max = float(female_weight_numbers[1])

print(female_weight_min)
print(female_weight_max)

# extracting female life expectancy as female life value 
female_life = border_collie_soup.find(id="female-life-value")
print(female_life.get_text())

# extracting male weight and life expectancy
male_weight = border_collie_soup.find(id="male-weight-value")
print(male_weight.get_text())

male_life = border_collie_soup.find(id="male-life-value")
print(male_life.get_text())