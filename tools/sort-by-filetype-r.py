import os
import shutil
import glob

# Ask the user for the directory to sort
dir_to_sort = input("Enter the directory: ")

# Define directories
image_dir = os.path.join(dir_to_sort, 'Images')
video_dir = os.path.join(dir_to_sort, 'Videos')
audio_dir = os.path.join(dir_to_sort, 'Audio')
archives_dir = os.path.join(dir_to_sort, 'Archives')
documents_dir = os.path.join(dir_to_sort, 'Documents')

# List of file extensions for each category
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico', '.heic', '.webp']
video_extensions = ['.webm', '.mp4', '.mov', '.flv', '.avi', '.mkv', '.wmv', '.rmvb', '.3gp','.m4v']
audio_extensions = ['.m4a', '.mp3', '.ogg', '.opus', '.flac', '.alac', '.wav', '.amr', '.aac', '.m4b', '.m4p']
archive_extensions = ['.zip', '.tar', '.tar.gz', '.rar','.tar', '.gz', '.7z'] 
document_extensions = ['.txt', '.doc', '.docx', '.pdf', '.ppt', '.pptx', '.xls', '.xlsx','.odt']

# Use glob to find all files in the directory and its subdirectories
files = glob.glob(dir_to_sort + '/**', recursive=True)

# Filter out directories
files = [file for file in files if os.path.isfile(file)]

# Iterate over each file
for file in files:
    # Get the file extension
    _, ext = os.path.splitext(file)
    ext = ext.lower()  # Convert to lowercase

    # Move the file to the appropriate directory based on its extension
    if ext in image_extensions:
        os.makedirs(image_dir, exist_ok=True)
        shutil.move(file, os.path.join(image_dir, os.path.basename(file)))
    elif ext in video_extensions:
        os.makedirs(video_dir, exist_ok=True)
        shutil.move(file, os.path.join(video_dir, os.path.basename(file)))
    elif ext in audio_extensions:
        os.makedirs(audio_dir, exist_ok=True)
        shutil.move(file, os.path.join(audio_dir, os.path.basename(file)))
    elif ext in archive_extensions:
        os.makedirs(archives_dir, exist_ok=True)
        # Move the archive file to the 'Archives' directory
        shutil.move(file, os.path.join(archives_dir, os.path.basename(file)))
    elif ext in document_extensions:
        os.makedirs(documents_dir, exist_ok=True)
        # Move the document file to the 'Documents' directory
        shutil.move(file, os.path.join(documents_dir, os.path.basename(file)))
