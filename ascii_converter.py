from PIL import Image

ASCII_CHARS = "@%#*+=-:. "
WIDTH = 100

def resize_image(image, new_width=WIDTH):
    width, height = image.size
    ratio = height / width / 1.65  # Adjust for font height
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")  # Convert to grayscale

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join(ASCII_CHARS[pixel // 25] for pixel in pixels)
    return ascii_str

def convert_image_to_ascii(path):
    try:
        image = Image.open(path)
    except:
        print("⚠️ Unable to open image.")
        return

    image = resize_image(image)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    img_width = image.width
    ascii_img = "\n".join([ascii_str[i:i+img_width] for i in range(0, len(ascii_str), img_width)])

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)

    print("\n✅ ASCII Art has been saved to 'ascii_image.txt'.")

if __name__ == "__main__":
    path = input("🖼️ Enter path to image file (e.g., example.jpg): ").strip()
    convert_image_to_ascii(path)
