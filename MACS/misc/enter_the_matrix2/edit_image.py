from PIL import Image, ImageOps
import cv2
import numpy as np
from pyzbar.pyzbar import decode


# Load the image
image_path = "glitch_matrix.png"  # Replace with your image path
image = Image.open(image_path)

# Convert the image to grayscale
image = image.convert("L")

# Threshold to convert red to black and black to white
threshold = 29  # Adjust the threshold as needed
image = image.point(lambda p: 0 if p < threshold else 255)

inverted_image = ImageOps.invert(image)


inverted_image.save("glitch_matrix3.png")