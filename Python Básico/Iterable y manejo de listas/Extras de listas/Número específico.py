print("---Número específico---")
print()

numbers_list = []
times_used = 0

while True:
    user_numbers = input("Por favor digite un número o escriba 'salir' para terminar el proceso cuando desee dejar de digitar números: ")
    if user_numbers == "salir":
        break
    numbers_list.append(int(user_numbers))

print()

number_to_look_for = int(input("Digite el número a buscar: "))

for numbers in numbers_list:
    if numbers == number_to_look_for:
        times_used += 1

print()

print(f'El número {number_to_look_for} aparece {times_used} veces.')
