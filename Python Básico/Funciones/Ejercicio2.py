#Intente acceder a una variable definida dentro de una función desde afuera.

def sum(number1, number2):
    defined_variable_local = number1 + number2
    return defined_variable_local

outside_variable_call = sum(20,30)
print(outside_variable_call)

#Intente acceder a una variable global desde una función y cambiar su valor.

#intento #1 que terminó en error

'''
global_variable = 2

def change_global():
    global_variable = 3
    print(global_variable)

change_global()
print(global_variable)
'''
#Correción de Lyfter
global_variable = 2

def change_global():
    global global_variable
    global_variable = 3

change_global()
print(global_variable)