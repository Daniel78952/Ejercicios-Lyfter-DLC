name = input("¿Cuál es su nombre?: ")
last_name = input("¿Cuál es su apellido?: ")
age = int(input("¿Cuál es su edad?: "))

if age <= 2:
    print(f"{name} {last_name} entra en la categoría de bebé.")
elif age <= 9:
    print(f"{name} {last_name} entra en la categoría de niño/niña.")
elif age <= 12:
    print(f"{name} {last_name} entra en la categoría de preadolescente.")
elif age <= 19:
    print(f"{name} {last_name} entra en la categoría de adolescente.")
elif age <= 29:
    print(f"{name} {last_name} entra en la categoría de adulto/adulta joven.")
elif age <= 59:
    print(f"{name} {last_name} entra en la categoría de adulto/adulta.")
else:
    print(f"{name} {last_name} entra en la categoría de adulto/adulta mayor.")
