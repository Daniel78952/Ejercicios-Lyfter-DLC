print("---Precio de Producto---")

price = int(input("Por favor, digite el precio del producto: "))
if price >= 100:
    discount = price * 0.10
    final_price= price - discount
else:
    discount = price * 0.02
    final_price = price - discount
print(f"El precio final es {final_price}.")