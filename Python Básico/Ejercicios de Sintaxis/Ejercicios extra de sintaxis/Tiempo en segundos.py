print("---Tiempo en Segundos---")

remaining_seconds = int(input("Introduzca los segundos: "))
if remaining_seconds == 600:
    print("Igual")
elif remaining_seconds > 600:
    print("Mayor")
else:
    remaining_seconds = 600 - remaining_seconds
    if remaining_seconds == 1:
        print(f"Falta {remaining_seconds}s para llegar a 10 minutos.")
    else:
        print(f"Faltan {remaining_seconds}s para llegar a 10 minutos.")