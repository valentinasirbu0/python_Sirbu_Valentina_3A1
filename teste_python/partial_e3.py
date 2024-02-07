'''
Write a Python script that:
● Reads a text file (5pts)
● Extracts the longest word (5pts)
● If multiple words with the same length, extract the one that is the first one in alphabetical
order (5pts)
● Extract the shortest word (5pts)
● If multiple words with the same length extract the one that is the last one in alphabetical
order (5pts)
● Calculate the average length of the words (5pts)
● Write the results in another file (5pts)
● The results will be saved in json format (5pts)
● In order to run the script, use a command line that has as argument the path of the file to be
read. (5pts)
● Check if the given file exists and handle errors (5pts)
● The script runs correctly and has a main function called (2pts)
● If the code is written in C style, you only get 75% of the maximum points per item
'''

import json
import os
import sys


def read_file(path):
    max_word = ""
    min_word = None
    nr_words = 0
    total_len = 0

    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            for word in line.split():
                nr_words += 1
                total_len += len(word)

                if len(word) > len(max_word):
                    max_word = word
                if len(word) == len(max_word):
                    if word < max_word:
                        max_word = word

                if min_word is None or len(word) < len(min_word):
                    min_word = word
                if len(word) == len(min_word):
                    if word < min_word:
                        min_word = word

    result = {
        "max len word": max_word,
        "min len word": min_word,
        "average len": total_len / nr_words
    }
    return result


def write_file(result):
    with open("file.json", 'w') as json_file:
        json.dump(result, json_file)


def main():
    if len(sys.argv) != 2:
        print("wrong parameters")
    else:
        if os.path.exists(sys.argv[1]) and os.path.isfile(sys.argv[1]):
            if len(read_file(sys.argv[1])) != 0:
                write_file(read_file(sys.argv[1]))
                print("succes")
            else:
                print("Blank file")


if __name__ == "__main__":
    main()
