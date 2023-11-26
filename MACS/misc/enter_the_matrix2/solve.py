from PIL import Image

def xor_strings(str1, str2):
    # Find the length of the shorter string
    length = min(len(str1), len(str2))

    # Perform XOR operation character by character up to the length of the shorter string
    result = ""
    for i in range(length):
        xor_result = ord(str1[i]) ^ ord(str2[i])
        result += chr(xor_result)

    return result

binary_string = ""
image = Image.open('glitch_matrix2.png')  # Replace with your image path

pixel_block_size = 2

# Get the dimensions of the image
width, height = image.size

for y in range(0, height, pixel_block_size):
    for x in range(0, width, pixel_block_size):
        # Define the boundaries for the current block
        x_end = min(x + pixel_block_size, width)
        y_end = min(y + pixel_block_size, height)

        # Track the count of black pixels in the block
        black_pixel_count = 0

        # Count black pixels in the current block
        for j in range(y, y_end):
            for i in range(x, x_end):
                pixel_color = image.getpixel((i, j))
                if pixel_color == (0,0,0,255):
                    black_pixel_count += 1

        # Determine if the majority of pixels in the block are black
        if black_pixel_count > (pixel_block_size * pixel_block_size) / 2:
            binary_string += '0'  # Add '1' for majority black blocks
        else:
            binary_string += '1'  # Add '0' for majority white blocks

# Print or use the binary string
binary_values = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]

# Convert each 8-bit binary value to ASCII
ascii_chars = ''.join([chr(int(binary, 2)) for binary in binary_values])

hint_string = "... hfb B ubvawlg anlb bu au mm xzwknbxf dnpv rqb yvqfr vt pzkqy izzkgjztwg"

print(ascii_chars)
print(xor_strings(hint_string, ascii_chars))