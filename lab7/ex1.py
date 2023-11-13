import sys
import os


def print_files(files):
    for fil in files:
        try:
            with open(fil) as f:
                contents = f.read()
                print(contents)
        except (PermissionError, IsADirectoryError) as e:
            print(f"Error accessing file {fil}: {e}")


arguments = sys.argv
res = []

try:
    if os.path.exists(arguments[1]):
        for file in os.listdir(arguments[1]):
            if file.endswith(arguments[2]):
                res.append(os.path.join(arguments[1], file))

        print_files(res)

        if not res:
            raise Exception(f"No files with the specified extension found")

    else:
        raise FileNotFoundError(f"The directory {arguments[1]} does not exist.")

except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")
