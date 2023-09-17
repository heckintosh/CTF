import random
import string
def find_matching_chars_with_indices(text1, text2):
    # Check if the input texts have the same length
    if len(text1) != len(text2):
        return "Input texts must have the same length."

    result = []

    # Iterate through the characters in both texts
    for i in range(len(text1)):
        char1 = text1[i]
        char2 = text2[i]

        # Compare characters at the same index
        if char1 == char2:
            result.append((i, char1))

    return result


def get_unique_chars(text):
    # Initialize an empty set to store unique characters
    unique_chars = set()

    # Iterate through the characters in the text
    for char in text:
        # Exclude '{' and '}' characters
        if char not in {'{', '}'}:
            unique_chars.add(char)

    # Convert the set to a list and return it
    unique_chars_list = list(unique_chars)
    return unique_chars_list


def randomly_chosen(text, seed):
    random.seed(seed)
    out = ''.join(random.choices(text, k=len(text)*5))
    return out


def generate_random_text(characters, length):
    # Check if the characters list is empty
    if not characters:
        return "Character list is empty."

    # Initialize an empty string to store the random text
    random_text = ""

    # Generate random text of the given length
    for _ in range(length):
        random_char = random.choice(characters)
        random_text += random_char

    return random_text


def replace_allowed_with_indices(text, allowed_characters):
    # Initialize an empty string to store the result
    result = ""

    # Iterate through the characters in the input text
    for char in text:
        # Replace allowed characters with their index in the allowed_characters list
        if char in allowed_characters:
            index = allowed_characters.index(char)
            result += str(index)
        else:
            result += '/'

    return result


def replace_allowed_with_char(text, allowed_characters):
    # Initialize an empty string to store the result
    result = ""

    # Iterate through the characters in the input text
    for char in text:
        # Replace allowed characters with their index in the allowed_characters list
        if char in allowed_characters:
            # index = allowed_characters.index(char)
            result += char
        else:
            result += '/'

    return result

def check_strings(input_text, str1, str2):
    if len(str1) != len(str2):
        return False

    # Create a set of characters from the input text
    input_set = set(input_text)

    # Check if both strings contain all characters from the input text
    if not input_set.issubset(set(str1)) or not input_set.issubset(set(str2)):
        return False

    # Check if the characters from the input text are at the same indices in both strings
    for char in input_text:
        if str1.index(char) != str2.index(char):
            return False

    return True

def find_matching_indices(string2, string1):
    # Initialize an empty dictionary to store the indices
    matching_indices = {}

    # Iterate through characters in string2
    for index, char in enumerate(string2):
        # Check if the character is present in string1
        if char in string1:
            # If it's present, add its index(s) to the dictionary
            indices = [i for i, c in enumerate(string1) if c == char]
            matching_indices[char] = indices

    return matching_indices


def list_contains_all_values(list1, list2):
    # Check if all values in list2 are present in list1
    return all(item in list1 for item in list2)


output = "bDacadn3af1b79cfCma8bse3F7msFdT_}11m8cicf_fdnbssUc{UarF_d3m6T813Usca?tf_FfC3tebbrrffca}Cd18ir1ciDF96n9_7s7F1cb8a07btD7d6s07a3608besfb7tmCa6sasdnnT11ssbsc0id3dsasTs?1m_bef_enU_91_1ta_417r1n8f1e7479ce}9}n8cFtF4__3sef0amUa1cmiec{b8nn9n}dndsef0?1b88c1993014t10aTmrcDn_sesc{a7scdadCm09T_0t7md61bDn8asan1rnam}sU"
print("Unique chars: ")

unique_chars = get_unique_chars(output)
print(unique_chars)
found = "DUCTF{i}"
# fake_flag = "DUCTF{" + generate_random_text(get_unique_chars(output), int(len(output)/5) - 7) + "}"
fake_flag = found + "/"*(60 - len(found))

seed = 252
pool = string.ascii_letters + string.digits + string.punctuation

while True:
    for k in unique_chars:
        tmp_found = found[:len(found) - 1] + k + found[len(found) - 1]
        fake_flag = tmp_found.removesuffix("}") + "/" * (61 - len(tmp_found)) + "}"
        guess = randomly_chosen(fake_flag, seed)
        indice1 = find_matching_indices(tmp_found, guess)
        indice2 = find_matching_indices(tmp_found, output)
        if list_contains_all_values(indice2[k], indice1[k]):
            print(replace_allowed_with_char(guess, tmp_found))
            print()
            print(output)
            found = tmp_found
            print(found)
            break
        
    