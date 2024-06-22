import os

def rename_to_capitalize_first_letter(directory):
    for entry in os.listdir(directory):
        original_path = os.path.join(directory, entry)
        if os.path.isdir(original_path):
            # Recursively rename subdirectories and their contents
            rename_to_capitalize_first_letter(original_path)
            # Rename directory itself to capitalize first letter
            new_name = entry.capitalize()
            new_path = os.path.join(directory, new_name)
            os.rename(original_path, new_path)
            print(f'Renamed directory {original_path} to {new_path}')
        else:
            # Rename files to capitalize first letter
            base_name, extension = os.path.splitext(entry)
            new_name = base_name.capitalize() + extension
            new_path = os.path.join(directory, new_name)
            os.rename(original_path, new_path)
            print(f'Renamed file {original_path} to {new_path}')

if __name__ == "__main__":
    # Prompt user to enter directory path
    directory = input("Enter the directory path: ").strip()
    
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        exit(1)
    
    rename_to_capitalize_first_letter(directory)
    print(f"All files and directories in {directory} have been renamed with first letter capitalized.")
