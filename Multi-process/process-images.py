import os
import concurrent.futures
from PIL import Image, ImageFilter
from decorators import RuntimePrinter

IMAGES_FOLDER_NAME = "images"


def process_image(img_name):
    size = (1200, 1200)
    img = Image.open(os.path.join(os.getcwd(), IMAGES_FOLDER_NAME, img_name))

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(os.path.join(os.getcwd(), "processed", img_name))
    print(f"{img_name} was processed...")


@RuntimePrinter
def process_images():
    img_names = os.listdir(os.path.join(os.getcwd(), IMAGES_FOLDER_NAME))

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, img_names)


def main():
    process_images()


if __name__ == "__main__":
    main()
