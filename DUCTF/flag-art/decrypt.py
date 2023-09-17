# Read the encrypted flag from output.txt
encrypted_flag = open('./output.txt', 'r').read()

# Reverse the palette to map the characters back to their original values
palette = '.=w-o^*'
reverse_palette = {char: str(index) for index, char in enumerate(palette)}

# Read the template from mask.txt
template = list(open('./mask.txt', 'r').read())

# Initialize variables
decrypted_flag = ''
index = 0

# Iterate through the encrypted flag
for char in encrypted_flag:
    # Find the corresponding palette character
    palette_char = reverse_palette[char]

    # Find the next 'X' in the template
    while index < len(template) and template[index] != 'X':
        index += 1

    # Replace the 'X' in the template with the palette character
    if index < len(template):
        template[index] = palette_char
        decrypted_flag += palette_char
        index += 1

# Print the decrypted flag
print(decrypted_flag)
