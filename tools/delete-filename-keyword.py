import os

def delete_files(directory, keyword):
    deleted_files = []
    
    # Get a list of all files in the directory
    files = os.listdir(directory)
    
    for file in files:
        filename = file.lower()
        
        # Check if the keyword is in the filename
        if keyword.lower() in filename:
            file_path = os.path.join(directory, file)
            try:
                os.remove(file_path)
                deleted_files.append(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
    
    if deleted_files:
        print("\nSummary of deleted files:")
        for file_path in deleted_files:
            print(f"- {file_path}")
    else:
        print("No files were deleted.")

if __name__ == "__main__":
    # Get the directory and keyword from the user
    directory = input("Enter the directory path: ").strip()
    keyword = input("Enter the keyword to delete files containing it: ").strip()
    
    delete_files(directory, keyword)
