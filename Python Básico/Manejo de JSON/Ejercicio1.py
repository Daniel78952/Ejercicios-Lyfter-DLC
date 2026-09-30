import json

def load_pokedex(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("No hay lista para leer")
        return []

def usr_hp():
    while True:
        try:
            hp = int(input('Digite los punto de vida del pokemon: '))
            break
        except ValueError:
            print("Debe digitar un número, no usar letras")
    return hp
def usr_skills():
    skills = []
    while True:
        inp_skills = input('Escriba las skills del pokemon o "salir" si ya terminó: ')
        if inp_skills == 'salir':
            break
        skills.append(inp_skills)
    return skills

def new_pokemon():
    pokemon = input('Escriba el nombre del pokemon o "salir" si ya terminó:: ')
    if pokemon == 'salir':
        return None
    
    poketype = input('Escriba el tipo de pokemon: ')
    hp = usr_hp()
    skills = usr_skills()


    poke_index = {
        "name" : pokemon,
        "type" : poketype,
        "hp" : hp,
        "skills" : skills
    }

    return poke_index

def finalized_pokedex():
    complete_poke_index = []
    while True:
        poke_index = new_pokemon()
        if poke_index is None:
            break
        complete_poke_index.append(poke_index)
    return complete_poke_index

def save_pokedex(path, data):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4,)

def main():
    path = 'Ejercicios Python/Manejo de JSON.json'
    pokedex = load_pokedex(path)
    pokedex+= finalized_pokedex()
    print(json.dumps(pokedex, indent=4))
    save_pokedex(path, pokedex)

main()

