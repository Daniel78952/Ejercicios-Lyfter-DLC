print('---Productos---')

products = [
    {"name": "Monitor", "category": "Gaming", "price": 200},
    {"name": "Teclado", "category": "Gaming", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Gaming", "price": 25},
    {"name": "Lavadora", "category": "Electrodomestica", "price": 80},
    {"name": "Mouse", "category": "Electrodomestica", "price": 35},
]

sales_by_category = {}

for product in products:
    if product['category'] in sales_by_category:
        sales_by_category[product['category']] += product['price']
    else:
        sales_by_category[product['category']] = product['price']

print(sales_by_category)