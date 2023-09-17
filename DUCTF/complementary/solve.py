from sympy import divisors

# Given product of m1 and m2
product = 6954494065942554678316751997792528753841173212407363342283423753536991947310058248515278

# Function to find possible pairs (m1, m2) given their product
def find_possible_pairs(product):
    possible_pairs = []
    for d in divisors(product):
        m1_candidate = d
        m2_candidate = product // d
        possible_pairs.append((m1_candidate, m2_candidate))
    return possible_pairs

# Find possible pairs of (m1, m2)
possible_pairs = find_possible_pairs(product)

# Decode and print the texts for each pair
for m1, m2 in possible_pairs:
    byte_data = (m1.to_bytes((m1.bit_length() + 7) // 8, byteorder='big') +
                 m2.to_bytes((m2.bit_length() + 7) // 8, byteorder='big'))
    decoded_text = byte_data.decode('utf-8', errors='ignore')
    print(f"Pair: (m1 = {m1}, m2 = {m2})")
    print(f"Decoded Text: {decoded_text}")
    print()
