import sqlite3
import statistics
import matplotlib.pyplot as plt
import numpy as np

# Foundational question:
# Is average dog breed weight associated with average life expectancy?
print("Foundational Question:")
print("Is dog breed weight associated with life expectancy?")
print()

connection = sqlite3.connect("dog_breeds.db")
cursor = connection.cursor()

cursor.execute("""
    SELECT breed_name, weight_midpoint_lbs, life_midpoint_years
    FROM dog_breeds
""")

breed_data = cursor.fetchall()

weights = []
lifespans = []

for breed in breed_data:
    weights.append(breed[1])
    lifespans.append(breed[2])

correlation = statistics.correlation(weights, lifespans)

print("Pearson correlation:", round(correlation, 3))

print("There is a negative association between dog breed weight and life expectancy.")
print("In this dataset, heavier dog breeds tend to have shorter life expectancies.")

plt.scatter(weights, lifespans)

slope, intercept = np.polyfit(weights, lifespans, 1)
trend_line = np.array(weights) * slope + intercept

plt.plot(weights, trend_line)

plt.xlabel("Breed Weight Midpoint (lbs)")
plt.ylabel("Life Expectancy Midpoint (years)")
plt.title("Dog Breed Weight vs. Life Expectancy")

plt.savefig("weight_vs_lifespan.png", bbox_inches="tight")
plt.show()