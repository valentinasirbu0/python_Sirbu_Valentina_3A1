'''
Write a script in Python that:
-reads a file containing text (5 pts);
- finds the longest word, the shortest word, the first word with its second letter b and the last
word with its last letter a (4 x 3 pts);
extract the unique words from the text (10 pts);
- sorts the unique words alphabetically
-> if the first letter of 2 words is the same, use their length as the sort criterion (10 pts);
- writes the answers in a file as "key: value" (the longest word, the shortest word, the counter of
unique words, the unique words sorted) (7 pts);
-parses a command line argument that represents the text file being read (sent using the argy
array by the user)
- run your script using the command line (passing the text file as an argument) and place the
command you used to run it in a comment inside your script (6 pts);
Notes:
- the code should run correctly and have a main function called (2 pts)
if the code is written in C style, you only get 75% of the maximum points per item!
Close
'''
import sys
from collections import Counter

#python partial2.py readme.txt


def read_file(file_name):
    with open(file_name, "r") as file:
        words = [word for line in file.readlines() for word in line.split()]

    longest = max(words, key=lambda item: len(item))
    shortest = min(words, key=len)
    second_b = [word for word in words if len(word) > 1 and word[1] == "b"]
    last_a = [word for word in words if word[-1] == "a"]

    dictionary = Counter(words)
    unique = list(word.lower() for word, occ in dictionary.items() if occ == 1)
    unique = sorted(unique, key=lambda item: (item[0], len(item)))

    result = {
        "longest : ": longest,
        "shortest : ": shortest,
        "second_b : ": second_b,
        "last_a : ": last_a[len(last_a)-1],
        "counter unique : ": len(unique),
        "unique words : ": unique
    }

    return result


def write_file(result):
    with open("file.txt", "w") as file:
        file.write(str(result))


def main():
    write_file(read_file(sys.argv[1]))


if __name__ == "__main__":
    main()

