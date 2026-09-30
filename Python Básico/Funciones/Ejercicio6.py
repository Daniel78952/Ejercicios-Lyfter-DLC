def alphabetical_order():
    user_string = input("Por favor escriba palabras separadas por un guión: ")
    create_list = user_string.split("-")
    create_list.sort()
    back_to_string = "-".join(create_list)
    return back_to_string

outside_list = alphabetical_order()
print(outside_list)