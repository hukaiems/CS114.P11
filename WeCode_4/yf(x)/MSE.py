import sys
import math
from sklearn.metrics import mean_squared_error
input_data = sys.stdin.read().strip()

x = []
y =[]

for number in input_data.splitlines():
    x_vals, y_vals = number.split(',')
    x_vals = float(x_vals)
    y_vals =float(y_vals)
    x.append(x_vals)
    y.append(y_vals)

y_hat = []
y_hat_teacher = []


for temp in x:
    a =1.8666281220550304e-15*temp**2 + -1.2306058315208687e-07*temp + 6.125593584307353
    y_hat.append(a)
    b = 1.6497423039747624e-07*temp + -2.4504033093402677*math.log2(temp) + 58.90213573241223
    y_hat_teacher.append(b)

Output = mean_squared_error(y, y_hat)
output_0 = mean_squared_error(y, y_hat_teacher)
print( f'Teacher: {output_0}    me:{Output}')