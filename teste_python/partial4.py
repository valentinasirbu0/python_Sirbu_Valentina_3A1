'''
Write a script in Python that:
- reads a file containing text (5 pts);
- extracts the positive and negative numbers from the text (10 pts);
- does the following operations on the extracted numbers: sum, min, max, avg(average) (4 x 3
pts);
- sorts them in descending order using the number of digits as the sort criterion;
-> if 2 numbers have the same number of digits, use their value as the sort criterion (10
pts);
- writes the answers in a file as "key: value" (7 pts);
- parses a command line argument that represents the text file being read (sent using the argv
array by the user)
- run your script using the command line (passing the text file as an argument) and place the
command you used to run it in a comment inside your script (6 pts).
Notes:
- the code should run correctly and have a main function called (2 pts)
- if the code is written in C style, you only get 75% of the maximum points per item!

'''
import sys
import json
#python partial4.py C:\Users\Valea\Desktop\teste_python\readme.txt


def read_file(path):
    with open(path, "r") as file:
        numbers = [num for line in file.readlines() for num in line.split() if num.isalpha() is not True]

    sum_num = sum(list(int(num) for num in numbers))
    min_num = min(list(int(num) for num in numbers))
    max_num = max(list(int(num) for num in numbers))
    avg_num = sum_num / len(numbers) if len(numbers) > 0 else " "

    numbers = sorted(numbers, key=lambda item: (len(item), int(item)))

    results = {
        "sum : ": sum_num,
        "min : ": min_num,
        "max : ": max_num,
        "avg : ": avg_num
    }

    return results


def write_file(result):
    with open("file.json", "w") as file:
        json.dump(result, file)


def main():
    write_file(read_file(sys.argv[1]))


if __name__ == "__main__":
    main()