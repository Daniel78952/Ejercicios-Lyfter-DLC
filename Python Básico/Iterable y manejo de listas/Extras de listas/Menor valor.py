print("---Menor valor---")
print()

numbers_list = []

while True:
    user_numbers = input("Por favor digite un número o escriba 'salir' para terminar el proceso cuando desee dejar de digitar números: ")
    if user_numbers == "salir":
        break
    numbers_list.append(int(user_numbers))

lowest_number = numbers_list[0]

for lowest in numbers_list:
    if lowest < lowest_number:
        lowest_number = lowest
print("El valor más bajo fue : ", lowest_number)