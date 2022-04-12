from PIL import Image


def img_to_greyscale(img_path: str):
    """Open an image and convert it to greyscale"""
    img = Image.open(img_path).convert('L')
    return img


def img_to_litho(img_path: str):
    """Take in an image path and other custom options to create a lithophane stl"""
    greyscale_img = img_to_greyscale(img_path)
    print(greyscale_img)
    return greyscale_img



def main():
    img_path = '/Users/chrisforsythe/Downloads/FullSizeRender.jpeg'
    greyscale_img = img_to_litho(img_path)
    greyscale_img.show()


if __name__ == '__main__':
    main()
