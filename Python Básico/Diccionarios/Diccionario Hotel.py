hotel_dictionary = {
    "name" : "Deep Sleep Resort",
    "rated_stars" : 5,
    "rooms" : [
        {
            "number" : 1,
            "floor" : 2,
            "price_per_night" : 120, 
        },
        {
            "number" : 2,
            "floor" : 2,
            "price_per_night" : 120,
        },
        {
            "number" : 3,
            "floor" : 3,
            "price_per_night" : 350,
        },
        {
            "number" : 4,
            "floor" : 4,
            "price_per_night" : 650,
        },
    ]
    }

for keys, values in hotel_dictionary.items():
    better_keys = keys.replace("_" , " ")
    if keys == 'rooms':
        print(f'{better_keys} :')
        for room in values:
            for info, roominfo in room.items():
                better_room_info = info.replace("_" , " ")
                print(f'{better_room_info} : {roominfo}')
    else:
        print(f'{better_keys} : {values}')

#Como no me gustaba que al imprimir Number_of_stars se vieran los "_"
#fui a google para ver que opciones existen para evitar eso, encontré el .replace