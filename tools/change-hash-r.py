import os
import hashlib
import sys

def calculate_hash(file_path):
 with open(file_path, 'rb') as f:
     bytes = f.read()
     return hashlib.md5(bytes).hexdigest()

def change_hash(file_path):
 with open(file_path, 'ab') as f:
     f.write(b'\0')

def main():
 directory_path = input("Enter the directory: ")

 for root, dirs, files in os.walk(directory_path):
     for filename in files:
         file_path = os.path.join(root, filename)
         old_hash = calculate_hash(file_path)
         change_hash(file_path)
         new_hash = calculate_hash(file_path)

         print(f'Old hash: {old_hash}, New hash: {new_hash}')

if __name__ == '__main__':
 main()
