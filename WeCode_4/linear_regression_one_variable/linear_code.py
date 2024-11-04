import sys

# em co tham khao kiem tra lai bang chat gpt cho chac a 
# em dua tren cong thuc em kiem duoc tren mang a 

input_data = sys.stdin.read().strip()

count = 0
x_total = 0
y_total = 0
x_squared_total = 0
xy_total = 0

for number in input_data.splitlines():
    x, y = number.split(',')
    x = float(x)
    y =float(y)
    x_total += x
    y_total += y
    count +=1
    x_squared_total += (x ** 2)
    xy_total += (x * y)

x_mean = x_total / count
y_mean = y_total / count

b = (xy_total - (count*x_mean*y_mean)) / (x_squared_total - count*(x_mean**2))
a = y_mean - b*x_mean

sys.stdout.write(f"{b} {a}")
