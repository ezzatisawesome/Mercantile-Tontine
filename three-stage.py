import numpy as np

def func(r1, r2):
    r3 = 100 / (100000 * r1 * r2)
    return -4400 * np.log((0.8*r1 - 0.2) * (0.8*r2 - 0.2) * (0.8*r3 - 0.2))

r1_values = np.linspace(0.01, 0.99, 100)
r2_values = np.linspace(0.01, 0.99, 100)

max_value = -np.inf
max_r1 = max_r2 = 0

for r1 in r1_values:
    for r2 in r2_values:
        try:
            value = func(r1, r2)
            if value > max_value:
                max_value = value
                max_r1, max_r2 = r1, r2
        except ValueError:
            continue

print(f"Maximum value: {max_value} found for r1 = {max_r1}, r2 = {max_r2}")
