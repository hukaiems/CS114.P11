def reverse_num(number):
    return number[::-1]

def is_palindrome(number):
    # em test thu code chatgpt
    length = len(number)

    for i in range (length//2):
        if number[i] != number[length - i - 1]:
            return False
    return True


    # code cu
    # if number == reverse_num(number):
    #     return True

import sys
input_data = sys.stdin.readline().strip()

# input_data = str(input())
result = 0
number_list = []

max_iterations = 10000
max_length = 15000

for i in range (max_iterations + 1):

    if len(input_data) > max_length:
        break

    reverse = reverse_num(input_data)
    input_data = str(int(input_data) + int(reverse))
    number_list.append(input_data)

    if is_palindrome(input_data):
        print("NO")
        for num in number_list:
            print(num)
        exit()

print("YES")
print(i)
print(number_list[-1])


