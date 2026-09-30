print("---Tabla de multiplicar---")

multiplied_by = 0
multiplier = int(input("Ingrese el número a multiplicar: "))

for multiplied_by in range (1,13):
    result = multiplier * multiplied_by
    print(f"{multiplier} x {multiplied_by} = {result}")