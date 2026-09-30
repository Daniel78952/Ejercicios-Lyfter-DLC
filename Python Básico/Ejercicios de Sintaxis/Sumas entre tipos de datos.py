#string + string= el resultado es que une ambos strings
number = "9"
name = "Daniel"
print(number + name)

#string + int= da fallo, un string solo se puede concatnar un str con otro str "can only concatenate str (not "int") to str", pero con * sí repite el str 'int' veces
"""
sis = "Sofía"
fav_number = 6
print(sis + fav_number)
"""
#int + string= mismo resultado que el caso anterior, aunque el error que da es diferente por el orden "unsupported operand type(s) for +: 'int' and 'str'"
"""
duck_number = 3
myself = "Mizt"
print(duck_number + myself)
"""
#list + list= en este caso ambas listas se suman/concatenan sin problemas

names_list = ["Sofía", "Alejandro", "Daniel"]
number_list = [8,14,6]
print(names_list + number_list)

#string + list= en este caso da el mismo error que al intentar hacer str+int
"""
leader = "Alejandro"
car_list = ["Hyundai", "Honda", "Ferrari"]
print(leader + car_list)
"""
#float + int= no presenta problemas, suma el float al int
pi = 3.14
jackpot = 100
print(pi + jackpot)

#bool + bool= en este caso el resultado es 1, esto se debe a que en Python True = 1 y False = 0
i_am_breathing = True
i_am_not_breathing = False
print(i_am_breathing + i_am_not_breathing)
