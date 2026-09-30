print("---First to last---")
print()

numbers = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6'
]

numbers[0], numbers[-1] = numbers [-1], numbers[0]
print(numbers)