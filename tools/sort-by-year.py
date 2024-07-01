import os
import shutil
from datetime import datetime

def organize_files_by_year(directory):
    # List all files in the directory (non-recursive)
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    for file in files:
        file_path = os.path.join(directory, file)

        # Get the last modification date of the file
        mtime = os.path.getmtime(file_path)
        last_modified_date = datetime.fromtimestamp(mtime)

        # Extract the year from the last modification date
        year = last_modified_date.year

        # Create a folder for the year if it doesn't exist
        year_folder = os.path.join(directory, str(year))
        if not os.path.exists(year_folder):
            os.makedirs(year_folder)

        # Move the file to the corresponding year folder
        destination_path = os.path.join(year_folder, file)
        shutil.move(file_path, destination_path)
        print(f"Moved '{file}' to {year_folder}")

if __name__ == "__main__":
    # Get the directory path from user input
    input_directory = input("Enter the directory: ")

    # Check if the input directory exists
    if not os.path.exists(input_directory):
        print("Error: The specified directory does not exist.")
    else:
        # Call the function to organize files by year
        organize_files_by_year(input_directory)
