print("---Número Mayor---")
print()
first_number = int(input("Por favor digita un número: "))
second_number = int(input("Por favor digita un número: "))
third_number = int(input("Por favor digita un número: "))
print()
if first_number >= second_number >= third_number:
    print(f"El número mayor es: {first_number}")
elif second_number >= first_number >= third_number:
    print(f"El número mayor es: {second_number}")
else:
    print(f"El número mayor es: {third_number}")
