def is_prime(number):
    count = 0
    for num in range(1, number+1):
        if number % num == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


def find_prime_in_list(input_list):
    prime_numbers = []
    for num in input_list:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers


lista = [0, 2, 4, 5, 6, 7, 8, 9]
r = find_prime_in_list(lista)
print(r)
