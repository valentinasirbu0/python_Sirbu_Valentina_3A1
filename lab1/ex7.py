#Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function will return 123, or if the text is "abc123abc" the function will extract 123). The function will extract only the first number that is found.
import re


def extract_number(text):
    match = re.search(r'\d+', text)

    if match:
        number = int(match.group())
        return number
    else:
        return None


text1 = "An apple is 123 USD"
result1 = extract_number(text1)
if result1 is not None:
    print(f"Extracted number: {result1}")
else:
    print("No number found in the text.")


text2 = "abc123abc"
result2 = extract_number(text2)
if result2 is not None:
    print(f"Extracted number: {result2}")
else:
    print("No number found in the text.")
