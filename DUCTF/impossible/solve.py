import numpy as np

import scipy.optimize as optimize
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, least_squares
from pwn import *
import ast
from scipy.optimize import fsolve
from sage.all import *
from sympy import symbols, Eq, solve, Mod


import math

def curve_model(x, a, b, p):
    return np.sqrt(x**3 + a*x + b) % p


# Initialize values for a and b



def is_square_rootable(value):
    """
    Checks if a value can be square-rooted (non-negative integer square root).

    Args:
        value: The value to be checked.

    Returns:
        True if the value can be square-rooted (non-negative integer square root),
        False otherwise.
    """
    # Check if the value is non-negative
    if value < 0:
        return False
    
    # Calculate the square root
    sqrt_value = math.sqrt(value)
    print(sqrt_value)
    # Check if the square root is an integer (not a floating-point number)
    return sqrt_value.is_integer()



def receive_points():
    # Replace with the address and port of the server you want to connect to
    host = 'misc-impossible-2fb66cb8eaca.2023.ductf.dev'
    port = 30000  # Replace with the server's port

    # Connect to the server
    r = remote(host, port)
    print(r.recvuntilS(b"\n>") + " R")
    # Receive points until an empty line is received
    r.sendline(b"R")
    print(r.recvuntilS(b"Username: ") + "heckintosh")
    r.sendline(b"heckintosh")
    print(r.recvuntilS(b"Public key: ") + "5")
    r.sendline(b"5")
    print(r.recvuntilS(b"\n>") + " L")
    r.sendline(b"L")
    print(r.recvuntilS(b"Username: ") + "heckintosh")
    r.sendline(b"heckintosh")

    points = r.recvuntilS(b"]")
    points = ast.literal_eval(points)
    
    # Replace these with your actual data
    x_data = np.array([x[0] for x in points])
    y_data = np.array([x[1] for x in points]) # Corresponding 100 y values
    
    initial_guess = [0, 0]

# Fit the curve to the data points using least-squares optimization
    result, covariance = curve_fit(curve_model, x_data, y_data, maxfev=250000)
    print(result)
    return points




if __name__ == '__main__':
    points = receive_points()
    # print("Received points:", received_points)


# Example usage:
# Define some points on an elliptic curve (replace with your actual points)
# points = [(1, 2), (3, 4), (5, 6)]
# curve = find_curve_through_points(points)
# print(curve)
