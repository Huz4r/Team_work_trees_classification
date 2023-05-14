from PIL import Image

class ImageRotator:
    def __init__(self, image_path):
        self.image_path = image_path
        self.angle = 0

    def rotate(self, angle):
        self.angle = angle
        image = Image.open(self.image_path)
        rotated_image = image.rotate(angle)
        rotated_image.show()
