import os
import sys


def count_files_by_extension(directory):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"The provided path '{directory}' is not a directory.")

        files = os.listdir(directory)

        if not files:
            raise ValueError(f"The directory '{directory}' is empty.")

        extension_count = {}

        for file in files:
            _, file_extension = os.path.splitext(file)
            extension_count[file_extension] = extension_count.get(file_extension, 0) + 1

        print("File count by extension:")
        for extension, count in extension_count.items():
            print(f"{extension}: {count} files")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        count_files_by_extension(directory_path)
