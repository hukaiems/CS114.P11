import math
import sys

input_data = sys.stdin.read().strip()

x_vals = []
y_vals = []

for number in input_data.splitlines():
    x, y = number.split(',')
    x = float(x)
    y = float(y)
    x_vals.append(x)
    y_vals.append(y)

N = len(x_vals)

# Update X matrix to include x^3 term
X = [[x**3, x**2, x, 1] for x in x_vals]

# Update XT matrix (transpose of X)
XT = [[X[j][i] for j in range(N)] for i in range(4)]

# Update XT_X and XT_y to handle the new dimensions
XT_X = [[sum(XT[i][k] * X[k][j] for k in range(N)) for j in range(4)] for i in range(4)]
XT_y = [sum(XT[i][k] * y_vals[k] for k in range(N)) for i in range(4)]

def matrix_d_3x3(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) -
            A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0]) +
            A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))

def matrix_d_4x4(A):
    return (
        A[0][0] * matrix_d_3x3([A[1][1:], A[2][1:], A[3][1:]]) -
        A[0][1] * matrix_d_3x3([[A[1][0]] + A[1][2:], [A[2][0]] + A[2][2:], [A[3][0]] + A[3][2:]]) +
        A[0][2] * matrix_d_3x3([[A[1][0], A[1][1], A[1][3]], [A[2][0], A[2][1], A[2][3]], [A[3][0], A[3][1], A[3][3]]]) -
        A[0][3] * matrix_d_3x3([A[1][:3], A[2][:3], A[3][:3]])
    )

def matrix_inverse_4x4(A):
    det = matrix_d_4x4(A)
    adj = [[0] * 4 for _ in range(4)]  # Initialize 4x4 matrix for adjugate
    
    # Fill adjugate matrix by computing minors and applying signs
    adj[0][0] =  matrix_d_3x3([A[1][1:], A[2][1:], A[3][1:]]) / det
    adj[0][1] = -matrix_d_3x3([[A[1][0]] + A[1][2:], [A[2][0]] + A[2][2:], [A[3][0]] + A[3][2:]]) / det
    adj[0][2] =  matrix_d_3x3([[A[1][0], A[1][1], A[1][3]], [A[2][0], A[2][1], A[2][3]], [A[3][0], A[3][1], A[3][3]]]) / det
    adj[0][3] = -matrix_d_3x3([A[1][:3], A[2][:3], A[3][:3]]) / det
    
    adj[1][0] = -matrix_d_3x3([A[0][1:], A[2][1:], A[3][1:]]) / det
    adj[1][1] =  matrix_d_3x3([[A[0][0]] + A[0][2:], [A[2][0]] + A[2][2:], [A[3][0]] + A[3][2:]]) / det
    adj[1][2] = -matrix_d_3x3([[A[0][0], A[0][1], A[0][3]], [A[2][0], A[2][1], A[2][3]], [A[3][0], A[3][1], A[3][3]]]) / det
    adj[1][3] =  matrix_d_3x3([A[0][:3], A[2][:3], A[3][:3]]) / det
    
    adj[2][0] =  matrix_d_3x3([A[0][1:], A[1][1:], A[3][1:]]) / det
    adj[2][1] = -matrix_d_3x3([[A[0][0]] + A[0][2:], [A[1][0]] + A[1][2:], [A[3][0]] + A[3][2:]]) / det
    adj[2][2] =  matrix_d_3x3([[A[0][0], A[0][1], A[0][3]], [A[1][0], A[1][1], A[1][3]], [A[3][0], A[3][1], A[3][3]]]) / det
    adj[2][3] = -matrix_d_3x3([A[0][:3], A[1][:3], A[3][:3]]) / det
    
    adj[3][0] = -matrix_d_3x3([A[0][1:], A[1][1:], A[2][1:]]) / det
    adj[3][1] =  matrix_d_3x3([[A[0][0]] + A[0][2:], [A[1][0]] + A[1][2:], [A[2][0]] + A[2][2:]]) / det
    adj[3][2] = -matrix_d_3x3([[A[0][0], A[0][1], A[0][3]], [A[1][0], A[1][1], A[1][3]], [A[2][0], A[2][1], A[2][3]]]) / det
    adj[3][3] =  matrix_d_3x3([A[0][:3], A[1][:3], A[2][:3]]) / det
    
    return adj

XT_X_inv = matrix_inverse_4x4(XT_X)

beta = [sum(XT_X_inv[i][j] * XT_y[j] for j in range(4)) for i in range(4)]

for i, x in enumerate(beta):
    if i == 0:
        sys.stdout.write(f'{x}*x**3 + ')
    elif i == 1:
        sys.stdout.write(f'{x}*x**2 + ')
    elif i == 2:
        sys.stdout.write(f'{x}*x + ')
    else:
        sys.stdout.write(f'{x}')
