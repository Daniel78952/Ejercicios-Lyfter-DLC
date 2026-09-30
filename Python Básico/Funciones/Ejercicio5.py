def upper_and_lower(string):
    upper_counter = 0
    lower_counter = 0
    for char in string:
        if char.isupper():
            upper_counter+=1
        elif char.islower():
            lower_counter+=1
    print(f"There's {upper_counter} upper cases and {lower_counter} lower cases.")

upper_and_lower("This Is A Test Of The Code.")