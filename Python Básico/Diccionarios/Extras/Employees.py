print('---Employees---')

employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Alex", "email": "alex@empresa.com", "department": "TI"},
    {"name": "Braian", "email": "braian@empresa.com", "department": "RRHH"},
    {"name": "Sofía", "email": "sofi@empresa.com", "department": "RRHH"},
    {"name": "Alejandro", "email": "alejo@empresa.com", "department": "TI"}
]

departments_info = {}

for employee in employees:
    if employee['department'] in departments_info:
        departments_info[employee['department']].append(employee['name'])
    else:
        departments_info[employee['department']]=[]
        departments_info[employee['department']].append(employee['name'])

print(departments_info)