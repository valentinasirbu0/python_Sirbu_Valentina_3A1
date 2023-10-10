#Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
import re

def camel_to_snake(input_string):
    snake_case = re.sub(r'([a-z])([A-Z])', r'\1_\2', input_string)
    snake_case = snake_case.lower()

    return snake_case


upper_camel_case_string = input("Enter a string in UpperCamelCase: ")

snake_case_string = camel_to_snake(upper_camel_case_string)
print(f"The string in lowercase_with_underscores is: {snake_case_string}")