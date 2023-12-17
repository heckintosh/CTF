def find_solutions(N, e):
  """
  This function finds all possible solutions for k and l that satisfy the equation:

  0 = x^2 + (1 - k*l(N - 1) + e)*x + k*l

  where:
    - N and e are integers and e is very large (up to 100 bits)
    - k and l are positive integers
    - 0 <= k + l < e
    - x can be either k or l

  Args:
    N: An integer.
    e: An integer.

  Returns:
    A list of tuples containing all possible solutions (k, l).
  """

  solutions = []
  # Loop through all possible values of k + l
  for kl_sum in range(e):
    # Find possible values of k and l that satisfy k + l = kl_sum
    for k in range(1, kl_sum + 1):
      l = kl_sum - k
      # Check if k and l are valid solutions
      if k > 0 and l > 0 and k*l(N - 1) + e < 1:
        # Check if x = k or x = l is a solution
        if k**2 + (1 - k*l*(N - 1) + e)*k + k*l == 0 or l**2 + (1 - k*l*(N - 1) + e)*l + k*l == 0:
          solutions.append((k, l))
  return solutions

# Get N and e from input
N = 0x78fb80151a498704541b888b9ca21b9f159a45069b99b04befcb0e0403178dc243a66492771f057b28262332caecc673a2c68fd63e7c850dc534a74c705f865841c0b5af1e0791b8b5cc55ad3b04e25f20dedc15c36db46c328a61f3a10872d47d9426584f410fde4c8c2ebfaccc8d6a6bd1c067e5e8d8f107b56bf86ac06cd8a20661af832019de6e00ae6be24a946fe229476541b04b9a808375739681efd1888e44d41196e396af66f91f992383955f5faef0fc1fc7b5175135ab3ed62867a84843c49bdf83d0497b255e35432b332705cd09f01670815ce167aa35f7a454f8b26b6d6fd9a0006194ad2f8f33160c13c08c81fe8f74e13e84e9cdf6566d2f
e = 0x4b3393c9fe2e50e0c76920e1f34e0c86417f9a9ef8b5a3fa41b381355

# Find all solutions
solutions = find_solutions(N, e)

# Print all solutions
print("All possible solutions:")
for k, l in solutions:
  print(f"k = {k}, l = {l}")

# Check if no solutions were found
if not solutions:
  print("No solutions found.")
