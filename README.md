# Encoding Text to Image and Decoding Image to Text

## Overview
This repository contains two Python scripts for:

1. **Encoding text into an image:**
   - Converts a given string into binary data and encodes it visually in an image.
2. **Decoding text from an image:**
   - Extracts encoded binary data from an image and converts it back into a readable string.

These scripts use **OpenCV** for image manipulation and **NumPy** for data processing.

---

## Features
### Encoding Script
- Converts text to a binary representation.
- Encodes the binary data into an image.
- Optionally accepts an input image to embed the text or generates a new blank image if none is provided.
- Saves the encoded image as `encoded_image.png`.

### Decoding Script
- Reads the binary data encoded in an image.
- Decodes the binary data into ASCII characters.
- Extracts the original text and saves it to a `.txt` file.

---

## Dependencies
Ensure the following Python libraries are installed before running the scripts:
- `opencv-python`
- `numpy`

Install the required libraries using pip:
```bash
pip install opencv-python numpy
```

---

## Usage

### Encoding Text to Image
#### Syntax:
```bash
python encoding_text_to_image.py [image_path] [text_file]
```
#### Parameters:
- `image_path`: (Optional) Path to an image file to embed the text into.
- `text_file`: (Optional) Path to a `.txt` file containing the text to encode.

#### Example:
1. **Without an image or text file**:
   ```bash
   python encoding_text_to_image.py
   ```
   You will be prompted to manually enter the text to encode.

2. **With an image and text file**:
   ```bash
   python encoding_text_to_image.py input_image.jpg input_text.txt
   ```
   The script will encode the text from `input_text.txt` into `input_image.jpg`.

3. **With only an image**:
   ```bash
   python encoding_text_to_image.py input_image.jpg
   ```
   You will be prompted to enter the text manually.

#### Output:
- The encoded image will be saved as `encoded_image.png` in the current directory.

---

### Decoding Image to Text
#### Syntax:
```bash
python decoding_image_to_text.py [image_path] [output_text_file]
```
#### Parameters:
- `image_path`: Path to the image containing encoded text.
- `output_text_file`: (Optional) Path to save the decoded text. Default is `output.txt`.

#### Example:
1. **With an image only**:
   ```bash
   python decoding_image_to_text.py encoded_image.png
   ```
   The decoded text will be saved in `output.txt`.

2. **With an image and custom output file**:
   ```bash
   python decoding_image_to_text.py encoded_image.png decoded_text.txt
   ```

#### Output:
- The decoded text will be saved in the specified text file.

---

## How It Works

### Encoding Process
1. **Text Conversion**:
   - The input string is converted to its ASCII values.
   - ASCII values are transformed into 7-bit binary representations.
2. **Binary Embedding**:
   - Each binary value (0 or 1) is embedded into the red channel of the image pixels.
   - If no image is provided, a blank image is generated.
3. **Termination Marker**:
   - A unique pixel marker `[1, 2, 3]` is added to indicate the end of the binary data.

### Decoding Process
1. **Binary Extraction**:
   - Reads the red channel of each pixel to retrieve the binary data.
   - Stops when the termination marker `[1, 2, 3]` is encountered.
2. **Binary Conversion**:
   - Groups binary data into chunks of 7 bits.
   - Converts each chunk back to its ASCII equivalent.

---

## Notes
- Ensure the image provided for encoding has enough pixels to store the binary data. If the text is too long, use a larger image.
- Avoid modifying the encoded image manually, as it may corrupt the binary data.

---

## Examples
### Encoding
Input:
```
Hello World!
```
Output:
- A generated or modified image (`encoded_image.png`) with encoded text.

### Decoding
Input:
- `encoded_image.png`
Output:
```
Hello World!
```

---

## Contributing
Feel free to fork the repository and submit pull requests for improvements or new features.

---

## Author
Developed by **Sabbu Sashidhar**. For any queries, feel free to reach out!
