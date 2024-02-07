'''
Using os.walk, write a script in Python that:
- reads all the file names from a directory (5 pts);
- finds the longest file name, the shortest file name, the first file name with its second letter c,
the last file name with its last letter c (2 x 6 pts);
- counts the number of files with each extension in the directory (10 pts);
-sorts the extensions in descending order based on their frequency
-> if 2 extensions have the same frequency, use their second letter as a sort criterion (10
pts);
- writes the answers in a file as "key: value" (7 pts);
- parses a command line argument that represents the directory being read (sent using the argy
array by the user)
- run your script using the command line (passing the directory path as an argument) and place
the command you used to run it in a comment inside your script (6 pts);
Notes:
the code should run correctly and have a main function called (2 pts)
if the code is written in C style, you only get 75% of the maximum points per item!
'''

import os
from collections import Counter
import sys


def read_files(dir_name):
    files = [file for root, dirs, files in os.walk(dir_name) for file in files]
    longest = max(files, key=len)
    shortest = min(files, key=len)
    second_c = [file for file in files if len(file) > 1 and file[1] == "c"]
    last_c = [file for file in files if file[-1] == "c"]

    extension_counter = Counter(file.split(".", 1)[-1] for file in files)
    counter = sorted(extension_counter.items(), key=lambda item: (-item[1], item[0][1]))

    result = {
        "longest : ": longest,
        "shortest : ": shortest,
        "second_c : ": second_c[0] if second_c else " ",
        "last_c : ": last_c[len(last_c)-1] if last_c else " "
    }

    return result


def write_file(result):
    with open("file.txt", "w") as file:
        file.write(str(result))


def main():
    write_file(read_files(sys.argv[1]))


if __name__ == "__main__":
    main()