from lithopy.img_to_litho import img_to_greyscale
from PIL import Image


def main():
    img_path = '/Downloads/FullSizeRender.jpeg'
    greyscale_img = img_to_greyscale(img_path)
    Image.show(greyscale_img)


if __name__ == '__main__':
    main()
