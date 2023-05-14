from PIL import Image
import os

# Open the image file
image = Image.open("H:\Python\Repozytoria\Team_work_trees_clasification\df\Original\Beech\IMG20211213122853.jpg")
# Get the resolution (width and height) of the image
width, height = image.size
print(f"Image resolution: {width}x{height}")
target_resolution = 512
rescale_value = 100 - (target_resolution / width)
print(f"Rescale value: {rescale_value}")
width = int(image.size[1] * rescale_value / 100)
height = int(image.size[0] * rescale_value / 100)
print(f"Image resolution: {width}x{height}")





'''
input_folder = "H:\Python\Repozytoria\Team_work_trees_clasification\df\Original\Pine"
output_folder = "H:\Python\Repozytoria\Team_work_trees_clasification\df\Trees_512_512\Pine"
new_size = (512, 512)  # Specify the desired size for the images

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate over the files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Open the image file
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)

        # Resize the image
        resized_image = image.resize(new_size)

        # Save the resized image to the output folder
        output_path = os.path.join(output_folder, filename)
        resized_image.save(output_path)

        # Close the image file
        image.close()

print("Image resizing and saving complete.")
'''