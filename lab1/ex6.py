#Write a function that validates if a number is a palindrome.
def is_palindrome(num):
    # Convert the number to a string to work with its digits
    num_str = str(num)

    # Reverse the string and compare it with the original
    return num_str == num_str[::-1]


# Example usage:
number = 1221
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
