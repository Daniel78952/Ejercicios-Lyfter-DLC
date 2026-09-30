print('---Verificador de positivos---')

list_to_check = [-6, 4, 5, 8, 0, -9, 5, 10, -3, -8]

for number in list_to_check:
    if number <= 0:
        print()
        print("Hay al menos un número negativo o cero.")
        break