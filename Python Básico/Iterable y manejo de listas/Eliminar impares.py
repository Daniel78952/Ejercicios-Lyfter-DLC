print("---Elimanar impares---")
print()

number_list = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
]

pairs =[]

for number in number_list:
    if number % 2 == 0:
        pairs.append(number)
print(pairs)