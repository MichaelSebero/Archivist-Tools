import os
import cv2
import numpy as np

def crop_image(img):
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold the image to get only the boundary pixels
    _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

    # Find contours in the image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour
    cnt = max(contours, key=cv2.contourArea)

    # Get the bounding rectangle for the contour
    x, y, w, h = cv2.boundingRect(cnt)

    # Crop the image using the bounding rectangle
    cropped = img[y:y + h, x:x + w]
    
    return cropped

def mass_crop(directory):
    # Get a list of all image files in the directory
    image_files = [f for f in os.listdir(directory) if f.endswith('.jpg') or f.endswith('.png')]

    for image_file in image_files:
        # Load the image
        img = cv2.imread(os.path.join(directory, image_file))

        # Crop the image
        cropped = crop_image(img)

        # Save the cropped image
        cv2.imwrite(os.path.join(directory, 'cropped_' + image_file), cropped)

if __name__ == '__main__':
    directory = input("Enter the directory path: ")
    mass_crop(directory)
