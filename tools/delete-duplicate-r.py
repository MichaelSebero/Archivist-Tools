import os
import hashlib

def calculate_file_hash(file_path):
   """Calculates the hash value of a file's content."""
   hasher = hashlib.md5()
   with open(file_path, 'rb') as file:
       for chunk in iter(lambda: file.read(4096), b''):
           hasher.update(chunk)
   return hasher.hexdigest()

def find_and_remove_duplicate_files(root_folder):
   """Traverses through the root folder and identifies duplicate files."""
   duplicates = {}
   for folder_path, _, file_names in os.walk(root_folder):
       for file_name in file_names:
           file_path = os.path.join(folder_path, file_name)
           file_hash = calculate_file_hash(file_path)
           if file_hash in duplicates:
               duplicates[file_hash].append(file_path)
           else:
               duplicates[file_hash] = [file_path]
   
   for file_paths in duplicates.values():
       if len(file_paths) > 1:
           print(f"Duplicate files found:\n{file_paths}\n")
           for file_path in file_paths[1:]:
               os.remove(file_path)
               print(f"{file_path} has been deleted.\n")

if __name__ == '__main__':
   root_folder = input("Enter the directory: ")
   find_and_remove_duplicate_files(root_folder)
