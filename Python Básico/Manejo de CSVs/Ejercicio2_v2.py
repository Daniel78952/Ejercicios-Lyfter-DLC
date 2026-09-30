import csv

def games_info(path, data):
    with open(path, 'w', encoding='utf-8', newline='') as file:

        headers = data[0].keys()

        writer = csv.DictWriter(file, fieldnames=headers, dialect='excel-tab')

        writer.writeheader()

        writer.writerows(data)

def usr_games():

    games = []

    while True:
        name = input("Escriba el nombre del juego (o escriba 'salir' para terminar.): ")
        if name == 'salir':
            break

        genre = input("Escriba el género del juego: ")
        developer = input("Escriba el nombre del desarrollador: ")

        while True:
            try:
                classification = float(input("Digite la nota: "))
                break
            except ValueError:
                print("Debe digitar un número, no usar letras")

        usr_game_data = {
            'Nombre' : name,
            'Género' : genre,
            'Desarrollador' : developer,
            'Clasificación' : classification
        }

        games.append(usr_game_data)
    return games

imputed_games = usr_games()
games_info('Ejercicios Python/Manejo de CSVs/games_usr_input_info_tab.csv', imputed_games)