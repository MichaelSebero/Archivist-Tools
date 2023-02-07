import os
import hashlib

def delete_duplicate_files(dir_path):
    # Create a dictionary to store files with the same name
    files = {}

    # Loop through all the files in the directory and subdirectories
    for root, dirs, filenames in os.walk(dir_path):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            file_size = os.path.getsize(file_path)

            # Calculate the SHA-1 hash of the file
            hasher = hashlib.sha1()
            with open(file_path, 'rb') as f:
                buf = f.read()
                hasher.update(buf)
            file_hash = hasher.hexdigest()

            # Add the file to the dictionary if the name and size are the same
            if filename in files:
                for f in files[filename]:
                    if f[0] == file_size and f[1] == file_hash:
                        os.remove(file_path)
                        break
                else:
                    files[filename].append((file_size, file_hash))
            else:
                files[filename] = [(file_size, file_hash)]

if __name__ == '__main__':
    dir_path = input('Enter the directory path: ')
    delete_duplicate_files(dir_path)
    print('Duplicate media files with the same name and size have been deleted.')
