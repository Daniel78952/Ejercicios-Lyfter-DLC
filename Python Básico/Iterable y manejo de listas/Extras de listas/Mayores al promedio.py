print('---Mayores al promedio---')
import random

num_list = num_list = random.sample(range(10, 101), 10)
total = sum(num_list)
average = total / 10

above_average = []

for number in num_list:
    if number > average:
        above_average.append(number)
print(f'Promedio: {average}')
print()
print(above_average)