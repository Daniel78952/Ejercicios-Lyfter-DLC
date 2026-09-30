print("---Dos listas a la vez---")

print()

first_list = [
    'Probando',
    'dos',
    'a la', 
    ]

second_list = [
    'imprimir',
    'listas',
    'vez',
]

for index, sentence in enumerate(first_list):
    print(sentence, second_list[index])