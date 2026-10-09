import requests
import sqlite3
from bs4 import BeautifulSoup

def calculate_midpoint(text, unit):
    cleaned_text = text.replace(unit, "")
    numbers = cleaned_text.split(" - ")

    minimum = float(numbers[0])
    maximum = float(numbers[1])

    midpoint = (minimum + maximum) / 2

    return midpoint

def scrape_breed(breed_url):
    response = requests.get(breed_url)
    soup = BeautifulSoup(response.text, "html.parser")

    female_weight = soup.find(id="female-weight-value")
    male_weight = soup.find(id="male-weight-value")
    female_life = soup.find(id="female-life-value")
    male_life = soup.find(id="male-life-value")

    if not female_weight or not male_weight or not female_life or not male_life:
        return None

    female_weight_avg = calculate_midpoint(female_weight.get_text(), " lbs")
    male_weight_avg = calculate_midpoint(male_weight.get_text(), " lbs")

    female_life_avg = calculate_midpoint(female_life.get_text(), " years")
    male_life_avg = calculate_midpoint(male_life.get_text(), " years")
    
    breed_weight_avg = (female_weight_avg + male_weight_avg) / 2
    breed_life_avg = (female_life_avg + male_life_avg) / 2
    
    breed_name = breed_url.split("/")[-1].replace("-", " ").title()

    return breed_name, breed_weight_avg, breed_life_avg


url = "https://dog-weight.com/breed-directory/"

response = requests.get(url) 
#print(response.status_code)  # Check if the request was successful

soup = BeautifulSoup(response.text, "html.parser")
#print(soup.title)

links = soup.find_all("a")
breed_links = []

for link in links:
    text = link.get_text(" ", strip=True)
    href = link.get("href")

    if href and "Weight:" in text and "Life expectancy:" in text:
        breed_links.append(href)

print(len(breed_links))
print(breed_links[:5])

# finding german shepherd breed link
# for breed_link in breed_links:
#     if "german" in breed_link:
#         print(breed_link)

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

# female_weight = border_collie_soup.find(id="female-weight-value")
# #print(female_weight) # we want to extract just the text from the element, not the entire tag
# print(female_weight.get_text())

# female_weight_text = female_weight.get_text()
# print(female_weight_text)

# female_weight_text = female_weight_text.replace(" lbs", "")
# print(female_weight_text)

# female_weight_numbers = female_weight_text.split(" - ")
# print(female_weight_numbers)

# female_weight_min = float(female_weight_numbers[0])
# female_weight_max = float(female_weight_numbers[1])

# print(female_weight_min)
# print(female_weight_max)

# # calculating the average weight of female border collies
# female_weight_avg = (female_weight_min + female_weight_max) / 2
# print(female_weight_avg)

# calculating female weight midpoint using function
female_weight = border_collie_soup.find(id="female-weight-value")
female_weight_avg = calculate_midpoint(female_weight.get_text(), " lbs")

print(female_weight_avg)

# extracting female life expectancy as female life value 
female_life = border_collie_soup.find(id="female-life-value")
# print(female_life.get_text())

# # we are doing this for years 

# female_life_text = female_life.get_text()
# female_life_text = female_life_text.replace(" years", "")
# female_life_numbers = female_life_text.split(" - ")

# female_life_min = float(female_life_numbers[0])
# female_life_max = float(female_life_numbers[1])

# female_life_avg = (female_life_min + female_life_max) / 2

# print(female_life_avg)

female_life_avg = calculate_midpoint(female_life.get_text(), " years")
print(female_life_avg)

# extracting male weight and life expectancy
male_weight = border_collie_soup.find(id="male-weight-value")
#print(male_weight.get_text())

male_life = border_collie_soup.find(id="male-life-value")
# print(male_life.get_text())

# male_weight_text = male_weight.get_text()
# male_weight_text = male_weight_text.replace(" lbs", "")
# male_weight_numbers = male_weight_text.split(" - ")

# male_weight_min = float(male_weight_numbers[0])
# male_weight_max = float(male_weight_numbers[1])

# male_weight_avg = (male_weight_min + male_weight_max) / 2
# print(male_weight_avg)

# calculating male weight midpoint using function
male_weight = border_collie_soup.find(id="male-weight-value")
male_weight_avg = calculate_midpoint(male_weight.get_text(), " lbs")

print(male_weight_avg)

# average weight of border collies (both male and female)
border_collie_weight_avg = (female_weight_avg + male_weight_avg) / 2
print(border_collie_weight_avg)
# testing the function to calculate the midpoint of a range of weights
# test_weight = calculate_midpoint("27 - 42 lbs", " lbs")
# print(test_weight)

border_collie_data = scrape_breed(border_collie_url)
print(border_collie_data)

# # testing german shepard breed
# german_shepherd_url = "https://dog-weight.com/german-shepherd"

# # german_shepherd_data = scrape_breed(german_shepherd_url)
# # print(german_shepherd_data)

# german_response = requests.get(german_shepherd_url)
# print(german_response.status_code)
# print(german_response.url)

second_breed_data = scrape_breed(breed_links[0])
print(second_breed_data)

breed_data = []

for breed_link in breed_links:
    data = scrape_breed(breed_link)

    if data is not None:
        breed_data.append(data)

print(len(breed_data))
print(breed_data[:5])


# creating a connection to the SQLite database
connection = sqlite3.connect("dog_breeds.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS dog_breeds (
    breed_name TEXT PRIMARY KEY,
    weight_midpoint_lbs REAL,
    life_midpoint_years REAL
    )
""")   

cursor.executemany("""
    INSERT OR REPLACE INTO dog_breeds 
    (breed_name, weight_midpoint_lbs, life_midpoint_years)
    VALUES (?, ?, ?)
""", breed_data)

# save the data to the database and close the connection
connection.commit()

cursor.execute("SELECT COUNT(*) FROM dog_breeds")
row_count = cursor.fetchone()[0]

print("Rows in database:", row_count)

connection.close()
