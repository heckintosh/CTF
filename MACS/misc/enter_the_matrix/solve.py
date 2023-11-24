from PIL import Image

# Load the image
image = Image.open('unknown_edit.png')  # Replace with your image path
image = image.convert('L')  # Convert to grayscale

binary_string = ""

# Apply threshold to convert to strictly black and white
threshold_value = 90 # Adjust this threshold value if needed
image = image.point(lambda p: 0 if p < threshold_value else 255, '1')

pixel_block_size = 10

# Get the dimensions of the image
width, height = image.size

# Initialize an empty binary string
binary_string = ''

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
                if pixel_color == 0:
                    black_pixel_count += 1

        # Determine if the majority of pixels in the block are black
        if black_pixel_count > (pixel_block_size * pixel_block_size) / 2:
            binary_string += '0'  # Add '1' for majority black blocks
        else:
            binary_string += '1'  # Add '0' for majority white blocks

# Print or use the binary string
print("Binary String:", binary_string)
binary_values = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]

# Convert each 8-bit binary value to ASCII
ascii_chars = ''.join([chr(int(binary, 2)) for binary in binary_values])

print(ascii_chars)