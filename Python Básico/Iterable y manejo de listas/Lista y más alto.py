print("---Lista y más alto---")
print()

numbers_list = []



for numbers in range(10):
    user_numbers = int(input("Por favor digite un número: "))
    numbers_list.append(user_numbers)

biggest_number = numbers_list[0]

for biggest in numbers_list:
    if biggest > biggest_number:
        biggest_number = biggest
print(numbers_list,"El numéro más alto fue : ", biggest_number)