import sys
import os

path = "/lab7\\ex2_1"


def rename_file(file, count):
    try:
        os.rename(path + "\\" + file, path + "\\file" + str(count) + ".txt")
    except PermissionError as e:
        print(f"Error accessing file")


try:
    if os.path.exists(path):
        count = 1
        for file in os.listdir(path):
            rename_file(file, count)
            count += 1

    else:
        raise FileNotFoundError(f"The directory does not exist.")

except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")
except PermissionError as e:
    print(f"Error: {e}")