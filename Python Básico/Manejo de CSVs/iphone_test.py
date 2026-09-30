import csv

def games_info(path, data):
    with open(path, 'w', encoding='utf-8-sig', newline='') as file:
        headers = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=';')
        writer.writeheader()
        writer.writerows(data)

games = [
    {
        "Nombre":"Grand Theft Auto IV",
        "Género":"Acción",
        "Desarrollador":"Rockstar",
        "Clasificación":"M",
    },
    {
        "Nombre":"The Elder Scrolls IV: Oblivion",
        "Género":"RPG",
        "Desarrollador":"Bethesda",
        "Clasificación":"M",
    },
    {
        "Nombre":"Tony Hawk's Pro Skater 2",
        "Género":"Deportes",
        "Desarrollador":"Activision",
        "Clasificación":"T",
    }
]

games_info('Ejercicios Python/Manejo de CSVs/games_superficial_info_iphone.csv', games)