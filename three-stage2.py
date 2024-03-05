import numpy as np
import math

def func(r):
    n = 3
    return -4400 * 3 * np.log(0.2*(1 - r) + r)

r_values = np.linspace(0.01, 0.99, 100)

max_value = -np.inf
max_r = 0

for r in r_values:
    try:
        value = func(r)
        print(value)
        if value > max_value:
            max_value = value
            max_r = r
    except ValueError:
        continue

print(f"Maximum value: {max_value} found for r = {max_r}")
