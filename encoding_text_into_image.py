import numpy as np
import math as m
import cv2
from tkinter import Tk, filedialog
import sys


# Helper Functions
def binary_conv(n):
    """Number to 7-digit binary converter."""
    s = ''
    while n > 1:
        s += str(n % 2)
        n //= 2
    s += str(n)
    s += "0" * (7 - len(s))
    return s


def string_to_binary(s):
    """Convert string to ASCII and ASCII to binary."""
    n = ''
    for i in s:
        n += binary_conv(ord(i))
    return n


def image(a, n=10,image_path=""):
    """Convert binary to image. 0=black, 1=white."""
    img_path=image_path
    if img_path:
        img = cv2.imread(img_path)
    else:
        img = np.zeros((n, n, 3), dtype=np.uint8)

    print(f"Image Shape: {img.shape}")
    c = 0
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if c == len(a):
                img[x][y] = [1, 2, 3]
                return img
            elif a[c] == '1' and img[x][y][0] < 125:
                img[x][y][0] = 126
            elif a[c] == "0" and img[x][y][0] > 125:
                img[x][y][0] = 124
            c += 1

    return img


def img_gen(text,image_path):
    """Convert string to binary, and binary to image."""
    binary_data = string_to_binary(text)
    print(f"Binary Data: {binary_data[:20]}.....")
    img = image(binary_data, int(m.sqrt(len(binary_data))) + 1,image_path)
    return img


# Main Execution
if __name__ == "__main__":
    script_name = sys.argv[0]
    text_to_encode=0
    if len(sys.argv)>1 and ("." in sys.argv[1]):
        if len(sys.argv)==2:
            image_path=sys.argv[1]
            print("image has been provided")
        elif len(sys.argv) == 3 and (".txt" in sys.argv[2]):
            image_path=sys.argv[1]
            text_file=sys.argv[2]
            with open("example.txt", "r") as file:
                text_to_encode = file.read()
            print("text has been provided")
        else:
            if len(sys.argv) >1:
                print("correct format is python encoding_text_to_image.py your_image.jpg your_textfile.txt")
                exit()
    else:
        if len(sys.argv) >1:
            print("correct format is python encoding_text_to_image.py your_image.jpg your_textfile.txt")
            exit()
        image_path="none"
    if image_path=="none":
        image_path=None
    if text_to_encode==0:
        text_to_encode = input("Enter the text to encode: ")
    image_np = img_gen(text_to_encode,image_path)
    # Show the generated image
    cv2.imshow("Encoded Image", image_np)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the generated image
    save_path = 'encoded_image.png'
    cv2.imwrite(save_path, image_np)
    print(f"Encoded image saved as '{save_path}'")
