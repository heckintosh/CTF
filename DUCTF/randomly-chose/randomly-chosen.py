import random

def find_matching_indices(string1, string2):
    indices = []
    for char in string2:
        if char in string1:
            indices.append(string1.index(char))
    
    return indices

# Example usage:



random.seed(252)
flag = open('./flag.txt', 'r').read().strip()
print(flag)
print()
out = ''.join(random.choices(flag, k=len(flag)*5))
print(out)


with open("output.txt", "r") as f:
    print()
    original = f.read().strip()
    print(original)

match = find_matching_indices(flag, original)

print(match)