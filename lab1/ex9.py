#Write a functions that determine the most common letter in a string. For example if the string is "an apple is not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a" represent the same character.
def most_common_letter(text):
    text = text.lower()

    letter_counts = {}

    for char in text:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1

    if letter_counts:
        most_common = max(letter_counts, key=letter_counts.get)

        return most_common, letter_counts[most_common]
    else:
        return None, 0


# Example usage:
text = "an apple is not a tomato"
most_common_letter, count = most_common_letter(text)
if most_common_letter is not None:
    print(f"The most common letter is '{most_common_letter}' ({count} times).")
else:
    print("No letters found in the text.")
