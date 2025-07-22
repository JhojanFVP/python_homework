# Task 2 imports
import csv
import os
from datetime import datetime
import traceback
import os
import custom_module  # Task 11

# Task 2: read_employees()
def read_employees():
    data = {'fields': [], 'rows': []}
    try:
        with open('../csv/employees.csv', newline='') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    data['fields'] = row
                else:
                    data['rows'].append(row)
    except Exception as e:
        raise e
    return data

employees = read_employees()
print(employees)

# Task 3: column_index()
employee_id_column = None
def column_index(col):
    return employees['fields'].index(col)

employee_id_column = column_index('employee_id')

# Task 4: first_name()
def first_name(rownum):
    idx = column_index('first_name')
    return employees['rows'][rownum][idx]

# Task 5: employee_find()
def employee_find(employee_id):
    def match(r): return int(r[employee_id_column]) == employee_id
    return list(filter(match, employees['rows']))

# Task 6: employee_find_2()
def employee_find_2(employee_id):
    return list(filter(lambda r: int(r[employee_id_column]) == employee_id, employees['rows']))

# Task 7: sort_by_last_name()
def sort_by_last_name():
    idx = column_index('last_name')
    employees['rows'].sort(key=lambda r: r[idx])
    return employees['rows']

print(sort_by_last_name())

# Task 8: employee_dict()
def employee_dict(row):
    return {field: val for field, val in zip(employees['fields'], row) if field != 'employee_id'}

print(employee_dict(employees['rows'][0]))

# Task 9: all_employees_dict()
def all_employees_dict():
    return {
        row[employee_id_column]: employee_dict(row)
        for row in employees['rows']
    }

print(all_employees_dict())

# Task 10: get_this_value()
def get_this_value():
    return os.getenv('THISVALUE')

# Task 11 has been covered via import & usage below
def set_that_secret(new):
    custom_module.set_secret(new)

set_that_secret("mysecret!")
print(custom_module.secret)

# Task 12: read_minutes()
def _read_csv(path):
    d = {'fields': [], 'rows': []}
    try:
        with open(path, newline='') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0: d['fields'] = row
                else: d['rows'].append(tuple(row))
    except Exception as e:
        raise e
    return d

minutes1, minutes2 = _read_csv('../csv/minutes1.csv'), _read_csv('../csv/minutes2.csv')
print(minutes1, minutes2)

# Task 13: create_minutes_set()
def create_minutes_set():
    return set(minutes1['rows']) | set(minutes2['rows'])

minutes_set = create_minutes_set()
print(minutes_set)

# Task 14: create_minutes_list()
def create_minutes_list():
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))

minutes_list = create_minutes_list()
print(minutes_list)

# Task 15: write_sorted_list()
def write_sorted_list():
    ml = create_minutes_list()
    ml.sort(key=lambda x: x[1])
    output = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), ml))
    with open('minutes.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(minutes1['fields'])
        writer.writerows(output)
    return output

print(write_sorted_list())
