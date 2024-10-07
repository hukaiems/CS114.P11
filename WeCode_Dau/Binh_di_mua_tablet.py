import math
input_data = float(input())

total = input_data*input_data

count = 0

# code cu cua em a
# for i in range (1, input_data):
#     i_2 = i*i
#     for j in range (i, input_data):
#         if i_2 + j*j == total:
#             # print(f"{i},{j}")
#             count += 1

# code cu cua em
# for i in range (2, input_data - 1):

# sau khi bi time limit lien tuc thi em tra hoi chatgpt va phat hien ra
# khong can chay den het tong gia tri ma chi can den can cua tong chia doi
limit_for = int(math.sqrt(total/2)) + 1

for i in range (1, limit_for):
    i_2 = i*i
    j_2 = total - i_2
    if j_2.isdigit() 
    count += 1

print(count)