# assignment4.py
import pandas as pd
import os

# --- Task 1.1: Create DataFrame ---
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(data)
print("\n--- Task 1.1 ---")
print(task1_data_frame)

# --- Task 1.2: Add Salary Column ---
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print("\n--- Task 1.2 ---")
print(task1_with_salary)

# --- Task 1.3: Increment Age ---
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print("\n--- Task 1.3 ---")
print(task1_older)

# --- Task 1.4: Save to CSV ---
csv_path = "employees.csv"
task1_older.to_csv(csv_path, index=False)
print(f"\n--- Task 1.4 ---\nCSV saved at {os.path.abspath(csv_path)}")



# --- Task 2.1: Load from CSV ---
task2_employees = pd.read_csv("employees.csv")
print("\n--- Task 2.1: Loaded CSV ---")
print(task2_employees)


import json

extra_employees = [
    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
]

with open("additional_employees.json", "w") as f:
    json.dump(extra_employees, f, indent=2)

# --- Task 2.2: Load from JSON ---
json_employees = pd.read_json("additional_employees.json")
print("\n--- Task 2.2: Loaded JSON ---")
print(json_employees)

# --- Task 2.3: Combine CSV + JSON ---
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("\n--- Task 2.3: Combined DataFrame ---")
print(more_employees)



# --- Task 3.1: First 3 rows ---
first_three = more_employees.head(3)
print("\n--- Task 3.1: First 3 Rows ---")
print(first_three)

# --- Task 3.2: Last 2 rows ---
last_two = more_employees.tail(2)
print("\n--- Task 3.2: Last 2 Rows ---")
print(last_two)

# --- Task 3.3: DataFrame shape ---
employee_shape = more_employees.shape
print("\n--- Task 3.3: Shape of DataFrame ---")
print(employee_shape)

# --- Task 3.4: DataFrame info ---
print("\n--- Task 3.4: DataFrame Info ---")
more_employees.info()



# --- Task 4.1: Load dirty data ---
dirty_data = pd.read_csv("dirty_data.csv")
print("\n--- Task 4.1: Dirty Data ---")
print(dirty_data)

# --- Task 4.2: Copy to clean_data ---
clean_data = dirty_data.copy()

# --- Task 4.3: Remove duplicate rows ---
clean_data = clean_data.drop_duplicates()
print("\n--- Task 4.3: After Dropping Duplicates ---")
print(clean_data)

# --- Task 4.4: Convert Age to numeric, handle missing ---
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print("\n--- Task 4.4: Age as Numeric (NaNs included) ---")
print(clean_data)

# --- Task 4.5: Convert Salary to numeric, replace placeholders with NaN ---
clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"], pd.NA)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print("\n--- Task 4.5: Salary Cleaned ---")
print(clean_data)

# --- Task 4.6: Fill missing values ---
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())
clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())
print("\n--- Task 4.6: Filled Missing Age and Salary ---")
print(clean_data)

# --- Task 4.7: Convert Hire Date to datetime ---
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")
print("\n--- Task 4.7: Hire Date Converted ---")
print(clean_data)

# --- Task 4.8: Strip whitespace and standardize Name and Department ---
clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()
print("\n--- Task 4.8: Standardized Name and Department ---")
print(clean_data)
