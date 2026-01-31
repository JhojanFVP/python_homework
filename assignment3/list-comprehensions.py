# list-comprehensions.py
import csv

with open("../csv/employees.csv") as f:
    reader = list(csv.reader(f))

# Skip header
header = reader[0]
rows = reader[1:]

# Full names
full_names = [f"{row[1]} {row[2]}" for row in rows]
print(full_names)

# Names containing 'e'
names_with_e = [name for name in full_names if "e" in name.lower()]
print(names_with_e)
