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
If the code is written in C style, you only get 75% of the maximum points per item
'''
from collections import Counter
from pathlib import Path

'''
def read_file():
    dictionary = Counter()

    with open("readme.txt", "r") as file:
        for line in file:
            words = line.split()
            dictionary.update(words)

    print(dictionary)
'''

import json
import os


def read_file():
    dictionary = {}

    with open("readme.txt", "r") as file:
        for line in file.readlines():
            for word in line.split():
                if (word[0].isupper() and word[1:].islower()) or word.islower():
                    word_lower = word.lower()
                    if word_lower in dictionary:
                        dictionary[word_lower] += 1
                    else:
                        dictionary[word_lower] = 1

    dic = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

    max_oc = max(dic.values())
    max_occ = [word for word, occurrences in dic.items() if occurrences == max_oc]

    min_oc = min(dic.values())
    min_occ = [word for word, occurrences in dic.items() if occurrences == min_oc]

    average_oc = sum(dic.values())
    average_occ = average_oc / len(dic)

    results = {
        "list of words with max occ: ": max_occ,
        "list of words with min occ: ": min_occ,
        "average occ: ":average_occ
    }
    return results


def write_file(result):
    path = Path("file.json")
    if os.path.isfile(path) and os.path.exists(path):
        with open("file.json", "w") as file:
            json.dump(result, file)


def main():
    write_file(read_file())


if __name__ == "__main__":
    main()
