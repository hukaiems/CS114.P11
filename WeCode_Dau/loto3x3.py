# em tham khao cach viet ham va cach tim vi tri cua gia tri trong
# ma tran tren chatgpt
def find_value_in_matrix(mnatrix, value):
    positions = []
    for i in range (3):
        for j in range(3):
            if matrix[i][j] == value:
                positions.append((i,j))
    return positions
matrix = []

# tham khao cach nhap tu chatgpt vi em khong biet cach nhap ma khong xuong dong
for i in range (3):
    a = input().split()
    matrix.append([int(x) for x in a])

# em tham khao cach tao ma tran rong trong python ngan gon tren chatpgt
matrix_2 = [[0 for _ in range(3)] for _ in range(3)]

total = int(input())

for i in range (total):
    a = int(input())
    # chatgpt huong dan em ap dung ham tim tren python a
    positions = find_value_in_matrix(matrix, a)
    if positions:
        for pos in positions:
            matrix_2[pos[0]][pos[1]] = 1


for i in range (3):
    if matrix_2[0][i] == matrix_2[1][i] == matrix_2[2][i] == 1:
        print("Yes")
        exit()
    elif matrix_2[i][0] == matrix_2[i][1] == matrix_2[i][2] == 1:
        print("Yes")
        exit()

if matrix_2[0][0] == matrix_2[1][1] == matrix_2[2][2] == 1:
    print("Yes")
elif matrix_2[0][2] == matrix_2[1][1] == matrix_2[2][0] == 1:
    print("Yes")
else:
    print("No")