def prime_identifier(number):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


def prime_printer(user_list):

    prime_list = []

    for number in user_list:
        save_prime = prime_identifier(number)
        if save_prime:
            prime_list.append(number)
    return prime_list

list_of__prime = prime_printer([41,56,82,64,95,26,17])

print(list_of__prime)