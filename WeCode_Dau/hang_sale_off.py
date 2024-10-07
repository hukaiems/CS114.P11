input_data = input().split()

count = len(input_data)

# print(count)

price_total = 0

for i in range (count):
    a = input()
    price_total += int(input_data[i])

total = input()

if int(total) >= price_total:
    print("true")
else:
    print("false")
