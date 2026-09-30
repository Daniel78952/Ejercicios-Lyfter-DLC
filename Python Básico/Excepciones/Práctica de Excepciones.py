# def main():
#     my_first_string = "2"
#     my_second_string = "Hello"

#     my_first_int = int(my_first_string)
#     print(my_first_int + 2)

#     my_second_int = int(my_second_string)
#     print(my_second_int + 2)

# if __name__ == '__main__':
#     main()


# def main():
#     my_second_string = "Hello"
#     try:
#         my_second_int = int(my_second_string)
#         print(my_second_int + 2)
#     except ValueError:
#         print('Hubo un error al convertir este string a numero!')

# if __name__ == '__main__':
#     main()

# try:
#     int("abc")
# except ValueError as e:
#     print(f"Error [ValueError]: No se pudo convertir el valor 'abc' a un entero. Detalles: {e}")

# try:
#     "2" + 2
# except TypeError as e:
#     print(f"Error [TypeError]: Intentaste combinar un string con un número. Detalles: {e}")

# try:
#     my_dict = {"a": 1}
#     value = my_dict["b"]
# except KeyError as e:
#     print(f"Error [KeyError]: La clave 'b' no existe en el diccionario. Detalles: {e}")

# try:
#     my_list = [1, 2, 3]
#     value = my_list[10]
# except IndexError as e:
#     print(f"Error [IndexError]: El índice 10 está fuera del rango de la lista. Detalles: {e}")

# try:
#     obj = 10
#     obj.some_method()
# except AttributeError as e:
#     print(f"Error [AttributeError]: El objeto de tipo 'int' no tiene el atributo 'some_method'. Detalles: {e}")

# try:
#     result = 10 / 0
# except ZeroDivisionError as e:
#     print(f"Error [ZeroDivisionError]: Intentaste dividir 10 entre 0. Detalles: {e}")


class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Fondos insuficientes: Intentaste retirar {amount}, pero solo tienes {balance} disponible.")

try:
    balance = 100
    amount_to_withdraw = 10
    if amount_to_withdraw > balance:
        raise InsufficientFundsError(balance, amount_to_withdraw)
except InsufficientFundsError as e:
    print(f"Error detectado: {e}")