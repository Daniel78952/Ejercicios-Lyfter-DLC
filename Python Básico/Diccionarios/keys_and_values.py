keys = [
    'first_name',
    'last_name' ,
    'role',
]

values = [
    'Fernando',
    'Zamora',
    'Product manager'
]

employee_info = {}

for info in range(len(keys)):
    employee_info[keys[info]] = values[info]
print(employee_info)