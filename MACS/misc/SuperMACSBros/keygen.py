import random
import string

def generate_key():
    # Generate 20 random uppercase alphanumeric characters
    first_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=22))

    while True:
        sum_first_part = sum(ord(char) for char in first_part)
        if 1600 <= sum_first_part <= 1700:
            print(first_part)
            print(sum_first_part)
            break
        else:
            # Regenerate the characters until the sum condition is met
            first_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=22))

    # Generate the remaining part until the total sum is 2050
    remaining_sum = 2050 - sum_first_part
    remaining_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    while True:
        sum_remaining_part = sum(ord(char) for char in remaining_part)
        if sum_remaining_part == remaining_sum:
            break
        else:
            remaining_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))

    # Concatenate the first 20 characters and the remaining 5 characters
    key = first_part + remaining_part

    return key

def validate_key(key):
    num = sum(ord(char) for char in key)
    return num == 2050

# Generate a valid key
valid_key = generate_key()
print(f"Generated Key: {valid_key}")

# Check if the generated key is valid according to the ValidateKey function
is_valid = validate_key(valid_key)
print(f"Is Valid Key: {is_valid}")
