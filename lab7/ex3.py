import sys
import os


def get_total_size(directory_path):
    total_size = 0

    try:
        for root, dirs, files in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                try:
                    file_size = os.path.getsize(file_path)
                    print(f"File Size of {file_path} in Bytes is {file_size}")
                    total_size += file_size
                except Exception as e:
                    print(f"Error accessing file {file_path}: {e}")

        print(f"Total Size of all files: {total_size} Bytes")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    get_total_size(directory_path)
