'''
Write a Python script that:
• Reads a text file (5pts)
• Counts the number of occurrences for each word - case insensitive (5pts)
• Counts only the words that are valid:
- contain only letters (5pts)
- all letters inside the word are lowercase - only the first letter may be uppercase (5pts)
• Extracts a list of words with the most occurrences (5pts)
• Extracts a list of words with the fewer occurrences (5pts)
• Computes the average number of occurrences (5pts)
• Writes the results in another file (5pts)
• The results will be saved in json format (5pts)
. Check if the given file exists and handle errors (5pts)
• The script runs correctly and has a main function called (2pts)
• If the code is written in C style, you only get 75% of the maximum points per item
'''

from collections import Counter
import json
import os
from pathlib import Path


def read_file():
    with open("readme.txt", "r") as file:
        dictionary = Counter([word.lower() for list in file.readlines() for word in list.split() if word.isalpha() and word[1:].islower() and( word[0].isupper() or word[0].islower())])

    most_occ = [word for word, occ in dictionary.items() if occ == max(dictionary.values())]
    least_occ = [word for word, occ in dictionary.items() if occ == min(dictionary.values())]
    average_occ = sum(dictionary.values()) / len(dictionary)

    result = {
        "most : ": most_occ,
        "least : ": least_occ,
        "average : ": average_occ
    }

    return result


def write_file(result):
    try:
        with open("file.json", "w") as file:
            json.dump(result, file)
    except FileNotFoundError:
        print("File not found")
        return None


def main():
    write_file(read_file())


if __name__ == "__main__":
    main()