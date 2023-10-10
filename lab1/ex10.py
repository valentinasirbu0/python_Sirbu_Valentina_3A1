#Write a function that counts how many words exists in a text. A text is considered to be form out of words that are separated by only ONE space. For example: "I have Python exam" has 4 words.
def count_words(text):
    words = text.split(' ')

    # Filter out empty strings (e.g., multiple spaces)
    #words = [word for word in words if word.strip()]

    return len(words)


# Example usage:
text = "I have Python exam"
word_count = count_words(text)
print(f"The text contains {word_count} words.")
