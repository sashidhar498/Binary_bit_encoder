import cv2
import sys

# Helper Functions
def deci_conv(n):
    """7-digit binary to decimal converter."""
    ans = 0
    for i in range(len(n)):
        ans += (2 ** i) * int(n[i])
    return ans


def image_to_bin(img):
    """Convert image to binary."""
    s = ''
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if img[x][y][0] > 125:
                s += '1'
            elif img[x][y][0] == 1 and img[x][y][1] == 2 and img[x][y][2] == 3:
                return s
            else:
                s += '0'
    return s


def img_to_string(img):
    """Convert image to binary, binary to ASCII, ASCII to string."""
    binary_data = image_to_bin(img)
    decoded_text = ""
    for i in range(len(binary_data) // 7):
        decoded_text += chr(deci_conv(binary_data[i * 7:(i + 1) * 7]))
    return decoded_text


# Main Execution
if __name__ == "__main__":
    script_name = sys.argv[0]
    text_to_encode=0
    file_name="output.txt"
    if len(sys.argv)>1 and ("." in sys.argv[1]):
        if len(sys.argv)==2:
            img_path=sys.argv[1]
            print("image has been provided")
        elif len(sys.argv) == 3 and (".txt" in sys.argv[2]):
            img_path=sys.argv[1]
            file_name=sys.argv[2]
            print("image and textfile has been provided")
        else:
            if len(sys.argv) >1:
                print("correct format is python Decoding_image_to_text.py your_image.jpg your_textfile.txt")
                exit()
    else:
        if len(sys.argv) >1:
            print("correct format is python Decoding_image_to_text.py your_image.jpg your_textfile.txt")
            exit()
    try:
        if img_path:
            image_np = cv2.imread(img_path)
            decoded_text = img_to_string(image_np)
            with open(file_name, "w") as file:
                file.write(decoded_text)

            print(f"Decoded Text saved in : {file_name}")
    except:
        print("No image selected. use python Decoding_image_to_text.py your_image.jpg your_textfile.txt")
