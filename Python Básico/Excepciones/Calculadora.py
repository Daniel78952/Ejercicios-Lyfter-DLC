def sum_calc(num1,num2):
    sum_to_be = num1 + num2
    return sum_to_be

def div_calc(num1,num2):
    div_to_be = num1 / num2
    return div_to_be

def res_calc(num1,num2):
    res_to_be = num1 - num2
    return res_to_be

def mul_calc(num1,num2):
    mul_to_be = num1 * num2
    return mul_to_be

def delete_result():
    return 0

def menu():
    print("1. Suma")
    print("2. Resta")
    print("3. División")
    print("4. Multiplicación")

    print("5. Borrar resultado")

    while True:
        try:
            user_choice = int(input("Digite una opción: "))
            if 1 <= user_choice <= 5:
                return user_choice
            else:
                print("Opción invalida, eliga un número del 1 al 5")
        except ValueError:
            print("Debe digitar el número tal como se ve en pantalla")

def main_calculator():
    numero_actual = 0
    while True:
        choice = menu()
        if choice == 1:
            try:
                print(numero_actual)
                usr_num = float(input("Número a sumar: "))
                numero_actual = sum_calc(numero_actual,usr_num)
                print(f'resultado: {numero_actual}')
            except ValueError:
                print("Debe digitar un número, no usar letras")
        elif choice == 2:
            try:
                print(numero_actual)
                usr_num = float(input("Número a restar: "))
                numero_actual = res_calc(numero_actual, usr_num)
                print(f'resultado: {numero_actual}')
            except ValueError:
                print("Debe digitar un número, no usar letras")
        elif choice == 3:
                    try:
                        print(numero_actual)
                        usr_num = float(input("Número a dividir: "))
                        numero_actual = div_calc(numero_actual, usr_num)
                        print(f'resultado: {numero_actual}')
                    except ZeroDivisionError:
                            print("No se puede dividir por 0")
                    except ValueError:
                        print("Debe digitar un número, no usar letras") 
        elif choice == 4:
                    try:
                        print(numero_actual)
                        usr_num = float(input("Número a multiplicar: "))
                        numero_actual = mul_calc(numero_actual, usr_num)
                        print(f'resultado: {numero_actual}')
                    except ValueError:
                        print("Debe digitar un número, no usar letras")
        elif choice == 5:
                    try:                        
                        numero_actual = delete_result()
                        print(numero_actual)
                    except ValueError:
                        print("Debe digitar un número, no usar letras")


main_calculator()