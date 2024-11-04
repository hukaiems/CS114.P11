import numpy as np
import sys
input_data = sys.stdin.read().strip()

x = []
y =[]

for number in input_data.splitlines():
    x_vals, y_vals = number.split(',')
    x_vals = float(x_vals)
    y_vals =float(y_vals)
    x.append(x_vals)
    y.append(y_vals)

n = len(x)


x_array = np.array(x)
y_array = np.array(y)

# Fit line
a, b = np.polyfit(x_array, y_array, 1)

print(f"Best fit line: y = {a}x + {b}")
