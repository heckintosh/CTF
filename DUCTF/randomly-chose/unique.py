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

# Example usage:
string1 = "helloo"
string2 = "world"
result = find_matching_indices(string1, string2)
print(result)
