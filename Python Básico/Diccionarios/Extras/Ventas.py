print("----Ventas---")

sales = [
    {
        'date' : '14/03/23',
        'customer_email' : 'phil@gmail.com',
        'items' : [
            {
                'name' : 'Uma Musume Acrylic',
                'upc' : 'ITEM-43',
                'unit_price' : 12,
            },
            {
                'name' : 'K-ON S1 BD',
                'upc' : 'ITEM-560',
                'unit_price' : 30,
            },
            {
                'name' : 'K-ON S2 BD',
                'upc' : 'ITEM-60',
                'unit_price' : 30,
            },
        ],
    },
    {
        'date' : '09/12/23',
        'customer_email' : 'darkrep@gmail.com',
        'items' : [
            {
                'name' : 'Holo Friends Plushie',
                'upc' : 'ITEM-633',
                'unit_price' : 35.20,
            },
            {
                'name' : 'K-ON S1 BD',
                'upc' : 'ITEM-560',
                'unit_price' : 30,
            },
            {
                'name' : 'Holo Friends Plushie',
                'upc' : 'ITEM-633',
                'unit_price' : 35.20,
            },
        ],
    },
    {
        'date' : '21/06/23',
        'customer_email' : 'darkrep@gmail.com',
        'items' : [
            {
                'name' : 'Holo Friends Plushie',
                'upc' : 'ITEM-633',
                'unit_price' : 35.20,
            },
            {
                'name' : 'K-ON S1 BD',
                'upc' : 'ITEM-560',
                'unit_price' : 30,
            },
            {
                'name' : 'K-ON MOVIE BD DLX',
                'upc' : 'ITEM-09',
                'unit_price' : 96.50,
            },
        ],
    },
    {
        'date' : '09/12/23',
        'customer_email' : 'al99@gmail.com',
        'items' : [
            {
                'name' : 'Uma Musume Acrylic',
                'upc' : 'ITEM-43',
                'unit_price' : 12,
            },
            {
                'name' : 'K-ON S1 BD',
                'upc' : 'ITEM-560',
                'unit_price' : 30,
            },
            {
                'name' : 'Holo Friends Plushie',
                'upc' : 'ITEM-633',
                'unit_price' : 35.20,
            },
        ],
    },
]

total_sales = {}



for sale in sales:
    for item in sale['items']:
        if item['upc'] in total_sales:
            total_sales[item['upc']] += item['unit_price']
        else:
            total_sales[item['upc']] = item['unit_price']

for upc, total in total_sales.items():
    print(f'{upc} : {total}')