import os
import shutil
from datetime import datetime
from PIL import Image
import piexif

# Supported image and video file types
IMAGE_EXTENSIONS = ('jpg', 'jpeg', 'png', 'heic')
VIDEO_EXTENSIONS = ('mp4', 'mov', 'avi', 'mkv')

# Function to get the date taken for images from EXIF metadata
def get_image_date_taken(file_path):
    try:
        image = Image.open(file_path)
        exif_data = image.info.get('exif')
        if exif_data:
            exif_dict = piexif.load(exif_data)
            date_taken = exif_dict.get('Exif', {}).get(piexif.ExifIFD.DateTimeOriginal)
            if date_taken:
                date_taken_str = date_taken.decode('utf-8')
                # Date format is "YYYY:MM:DD HH:MM:SS", we only care about "YYYY" and "MM"
                date_taken_obj = datetime.strptime(date_taken_str, "%Y:%m:%d %H:%M:%S")
                return date_taken_obj
    except Exception as e:
        print(f"Could not extract date for {file_path}: {e}")
    return None

# Function to get the last modified date for videos
def get_video_date_taken(file_path):
    try:
        last_modified_time = os.path.getmtime(file_path)
        date_taken = datetime.fromtimestamp(last_modified_time)
        return date_taken
    except Exception as e:
        print(f"Could not extract date for {file_path}: {e}")
    return None

# Function to organize files by date into year/month and Images/Videos subfolders
def organize_by_date(src_dir, recursive=False):
    # Walk through all files in the source directory (and subdirectories if recursive is enabled)
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            # Get full path of the file
            file_path = os.path.join(root, file)
            date_taken = None
            media_type = None

            # Check if the file is an image and get the capture date from EXIF metadata
            if file.lower().endswith(IMAGE_EXTENSIONS):
                date_taken = get_image_date_taken(file_path)
                media_type = "Images"
            # Check if the file is a video and get the last modified date
            elif file.lower().endswith(VIDEO_EXTENSIONS):
                date_taken = get_video_date_taken(file_path)
                media_type = "Videos"

            # If a date was found, organize the file by that date
            if date_taken:
                # Extract the year and month from the date taken
                year = date_taken.strftime("%Y")
                month = date_taken.strftime("%B")

                # Create directories for year, month, and media type (Images/Videos) if they don't exist
                year_dir = os.path.join(src_dir, year)
                month_dir = os.path.join(year_dir, month)
                media_dir = os.path.join(month_dir, media_type)

                if not os.path.exists(media_dir):
                    os.makedirs(media_dir)

                # Move the file to the respective directory
                shutil.move(file_path, os.path.join(media_dir, file))
                print(f'Moved {file} to {media_dir}')
            else:
                print(f"Date taken not found for {file}, skipping...")

        # If recursive is not enabled, break after the first directory
        if not recursive:
            break

if __name__ == "__main__":
    # Prompt the user to input the source directory
    source_directory = input("Enter the directory where the files are located: ").strip()
    
    # Ask if the user wants recursive sorting
    recursive_option = input("Do you want to sort files in subdirectories recursively? (y/n): ").strip().lower()
    recursive = True if recursive_option == 'y' else False

    # Ensure the entered path exists
    if not os.path.exists(source_directory):
        print("Source directory does not exist. Please enter a valid path.")
    else:
        organize_by_date(source_directory, recursive)
        print("Sorting complete.")
