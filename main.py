from PIL import Image
import os
from keras.preprocessing.image import ImageDataGenerator
from classes import *

# Open the image file
path_to_image = 'IMG20211213122853.jpg'
image = Image.open(path_to_image)
# Get the resolution (width and height) of the image
width, height = image.size
print(f"Image resolution: {width}x{height}")
target_resolution = 512
rescale_value = 100 - (target_resolution / width)
print(f"Rescale value: {rescale_value}")
width = int(image.size[1] * rescale_value / 100)
height = int(image.size[0] * rescale_value / 100)
print(f"Image resolution: {width}x{height}")





# Create an instance of the ImageRotator class
rotator = ImageRotator(path_to_image)

# Rotate the image by x degrees
rotator.rotate(3)

# Print the current angle of rotation
print(rotator.angle)