import random

secret_number = random.randint(1, 10)
print("¡Intenta adivinar un el número del 1 al 10!")
print()
usr_attempt = 0
while usr_attempt != secret_number:
    usr_attempt = int(input("Digita aquí tú respuesta: "))
    if usr_attempt != secret_number:
        print("¡Fallaste! ¡Intenta de nuevo!")
print("¡Adivinaste el número!")