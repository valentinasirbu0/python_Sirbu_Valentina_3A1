def generate_fibonacci(n):
    fibonacci_list = []
    if n <= 0:
        return fibonacci_list
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci_list = [0, 1]
        while len(fibonacci_list) < n:
            next_number = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(next_number)
        return fibonacci_list


# Example usage:
number = 10  # Change this value to get the first n Fibonacci numbers
result = generate_fibonacci(number)
print(result)
