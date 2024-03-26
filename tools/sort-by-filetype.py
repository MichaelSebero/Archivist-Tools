import os
import shutil
import zipfile
import tarfile

# Ask the user for the directory to sort
dir_to_sort = input("Enter the directory: ")

# Define directories
image_dir = os.path.join(dir_to_sort, 'Images')
video_dir = os.path.join(dir_to_sort, 'Videos')
audio_dir = os.path.join(dir_to_sort, 'Audio')
archive_dir = os.path.join(dir_to_sort, 'Archives')
document_dir = os.path.join(dir_to_sort, 'Documents')

# List of file extensions for each category
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico', '.heic', '.webp']
video_extensions = ['.webm', '.mp4', '.mov', '.flv', '.avi', '.mkv', '.wmv', '.rmvb', '.3gp','.m4v']
audio_extensions = ['.m4a', '.mp3', '.ogg', '.opus', '.flac', '.alac', '.wav', '.amr', '.aac', '.m4b', '.m4p']
archive_extensions = ['.zip', '.tar', '.tar.gz', '.rar','.tar', '.gz', '.7z']
document_extensions = ['.txt', '.doc', '.docx', '.pdf', '.ppt', '.pptx', '.xls', '.xlsx','.odt']

# Get list of files in the directory
files = os.listdir(dir_to_sort)

# Initialize counters for each category
image_count = 0
video_count = 0
audio_count = 0
archive_count = 0
document_count = 0

# Iterate over each file
for file in files:
    # Get the file extension
    _, ext = os.path.splitext(file)
    ext = ext.lower()  # Convert to lowercase

    # Count the file based on its extension
    if ext in image_extensions:
        image_count += 1
    elif ext in video_extensions:
        video_count += 1
    elif ext in audio_extensions:
        audio_count += 1
    elif ext in archive_extensions:
        archive_count += 1
    elif ext in document_extensions:
        document_count += 1

# Create directories only if they contain files
if image_count > 0:
    os.makedirs(image_dir, exist_ok=True)
if video_count > 0:
    os.makedirs(video_dir, exist_ok=True)
if audio_count > 0:
    os.makedirs(audio_dir, exist_ok=True)
if archive_count > 0:
    os.makedirs(archive_dir, exist_ok=True)
if document_count > 0:
    os.makedirs(document_dir, exist_ok=True)

# Reset the file list
files = os.listdir(dir_to_sort)

# Iterate over each file again to move them
for file in files:
    # Get the file extension
    _, ext = os.path.splitext(file)
    ext = ext.lower()  # Convert to lowercase

    # Move the file to the appropriate directory based on its extension
    if ext in image_extensions:
        shutil.move(os.path.join(dir_to_sort, file), os.path.join(image_dir, file))
    elif ext in video_extensions:
        shutil.move(os.path.join(dir_to_sort, file), os.path.join(video_dir, file))
    elif ext in audio_extensions:
        shutil.move(os.path.join(dir_to_sort, file), os.path.join(audio_dir, file))
    elif ext in archive_extensions:
        shutil.move(os.path.join(dir_to_sort, file), os.path.join(archive_dir, file))
    elif ext in document_extensions:
        shutil.move(os.path.join(dir_to_sort, file), os.path.join(document_dir, file))
