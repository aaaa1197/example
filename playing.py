print("Helllo world")

a = ( 1 * (1 +  2))

for i in range(10):
    print(i)

import numpy as np

x = np.array([1, 2, 3])

# Create a 3x3 array of all ones
m = np.ones((3, 3))

# Operate on x with m
y = np.dot(m, x)   

print(y)

# A function which evaluates a quadratic
def evaluate_quadratic(x, a=0, b=0, c=0):
    return a * x**2 + b * x + c

def evaluate_cubic(x, a=0, b=0, c=0, d=0):
    '''Evaluate a cu bic polynomial at x with coefficients a, b, c, and d.
    :param x: The point at which to evaluate the polynomial.
    :param a: The coefficient of the cubic term.
    :param b: The coefficient of the quadratic term.
    :param c: The coefficient of the linear term.
    :param d: The constant coefficient.'''
    return a * x**3 + b * x**2 + c * x + d

z = [i for i in range(10) if i % 2 == 0]

