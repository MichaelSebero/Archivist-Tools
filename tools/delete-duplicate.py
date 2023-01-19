import os
import hashlib
from pathlib import Path

def remove_duplicates(directory):
 unique_files = dict()
 list_of_files = os.listdir(directory)
 
 for file in list_of_files:
    file_path = Path(os.path.join(directory, file))
    if file_path.is_file():
        try:
            Hash_file = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
        except (FileNotFoundError, PermissionError) as e:
            print(f"Failed to open {file_path}: {e}")
            continue

        if Hash_file not in unique_files:
            unique_files[Hash_file] = file_path
        else:
            os.remove(file_path)
            print(f"{file_path} has been deleted")

def main():
 directory = input("Enter the directory: ")
 remove_duplicates(directory)

if __name__ == "__main__":
 main()
