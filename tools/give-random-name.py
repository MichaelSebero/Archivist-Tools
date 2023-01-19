import os
import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def rename_files_in_directory(directory_path):
    for entry in os.scandir(directory_path):
        if entry.is_file():
            # Generate a new random name with  8 characters
            new_name = generate_random_string(8) + os.path.splitext(entry.name)[1]
            new_path = os.path.join(directory_path, new_name)
            
            # Rename the file
            os.rename(entry.path, new_path)

# Prompt the user for the directory path
directory_path = input('Enter the directory: ')

# Check if the directory exists
if os.path.exists(directory_path):
    rename_files_in_directory(directory_path)
else:
    print('The specified directory does not exist. Please check the path and try again.')
