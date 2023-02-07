import os
import hashlib

def get_hash(filename):
    """Calculate hash value of a file"""
    hasher = hashlib.sha1()
    with open(filename, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def delete_duplicates(directory):
    """Delete media files with the same name and size"""
    file_hashes = {}
    deleted = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_hash = get_hash(file_path)
            if file_hash in file_hashes:
                os.remove(file_path)
                deleted += 1
            else:
                file_hashes[file_hash] = file_path
    print(f"Deleted {deleted} files.")

directory = input("Enter the directory path: ")
delete_duplicates(directory)
