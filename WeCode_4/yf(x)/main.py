# em da tham khao qua chatgpt de co duoc doan code nay a 
# day la cac cau prompt cua em 
# n linear regression 

# prompt 1
# i got data points (x,y)
# now i need to find the function y = f(x)
# to have the smallest MSE

# i try y = ax+b but it not enough 
# can you give me some advice 
# like are there any other way 
# and if it is provide me the highlighted name and the math to calculate all the element of that way 
# thank you 


# prompt 2
# how about a function like ax +b*log2(x) + c
# what can i call a function like that 

# prompt 3
# so from the data points to that function 
# how can i calculate it step by step for all the element

# so how does it work
# like it a list 
# then can u visualize what inside the X list for me ?

# prompt 5
# okay how to do step 3?

# prompt 6
# and can you show me the formula when written in math ?

# prompt 7
# this is my code but the MSE is still too high so how can minimize the MSE more
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


X = [[x**2, x, 1] for x in x_vals]  

XT = [[X[j][i] for j in range(N)] for i in range(3)]
XT_X = [[sum(XT[i][k] * X[k][j] for k in range(N)) for j in range(3)] for i in range(3)]
XT_y = [sum(XT[i][k] * y_vals[k] for k in range(N)) for i in range(3)]

def matrix_d_3x3(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) -
            A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0]) +
            A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))

def matrix_inverse_3x3(A):
    det = matrix_d_3x3(A)
    
    adj = [
        [(A[1][1] * A[2][2] - A[1][2] * A[2][1]) / det,
         (A[0][2] * A[2][1] - A[0][1] * A[2][2]) / det,
         (A[0][1] * A[1][2] - A[0][2] * A[1][1]) / det],
        
        [(A[1][2] * A[2][0] - A[1][0] * A[2][2]) / det,
         (A[0][0] * A[2][2] - A[0][2] * A[2][0]) / det,
         (A[0][2] * A[1][0] - A[0][0] * A[1][2]) / det],
        
        [(A[1][0] * A[2][1] - A[1][1] * A[2][0]) / det,
         (A[0][1] * A[2][0] - A[0][0] * A[2][1]) / det,
         (A[0][0] * A[1][1] - A[0][1] * A[1][0]) / det]
    ]
    return adj

XT_X_inv = matrix_inverse_3x3(XT_X)

beta = [sum(XT_X_inv[i][j] * XT_y[j] for j in range(3)) for i in range(3)]

for i, x in enumerate(beta):
    if i == 0:
        sys.stdout.write(f'{x}*x**2 + ')
    elif i == 1:
        sys.stdout.write(f'{x}*x + ')
    else:
        sys.stdout.write(f'{x}')