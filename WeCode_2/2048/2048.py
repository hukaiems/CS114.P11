import sys
# em co su dung chatgpt de kiem tra ki cac dieu kien tranh sai sot a
matrix = []

for i in range(4): 
    input_data = sys.stdin.readline().split()
    matrix.append(input_data)

input_2 = input()

if input_2 == 'L':
    for i in range(4):
        flag = 0
        for j in range(1, 4): 
            # duyet tung cot 1 den 3 vi cot 0 da co dk kiem tra ben trong
            while j != 0:
                if j - 1 >= 0 and j < 4:
                    if matrix[i][j-1] == matrix[i][j] == '0':
                        break
                    if matrix[i][j - 1] == '0' or matrix[i][j - 1] == matrix[i][j] and flag == 0:
                        if matrix[i][j-1] == matrix[i][j]:
                            flag = 1
                        matrix[i][j - 1] = str(int(matrix[i][j - 1]) + int(matrix[i][j]))
                        matrix[i][j] = '0'
                j -= 1
                # print(*matrix[i])
                # print(flag)


elif input_2 == 'R':
    for i in range(4):
        flag = 0
        for j in range(2, -1, -1): 
            # duyet tung cot 1 den 3 vi cot 0 da co dk kiem tra ben trong
            while j != 3:
                if j + 1 < 4 and j >= 0:
                    if matrix[i][j + 1] == matrix[i][j] == '0':
                        break
                    if matrix[i][j + 1] == '0' or matrix[i][j + 1] == matrix[i][j] and flag == 0:
                        if matrix[i][j+1] == matrix[i][j]:
                            flag = 1
                        matrix[i][j + 1] = str(int(matrix[i][j + 1]) + int(matrix[i][j]))
                        matrix[i][j] = '0'
                j += 1
                # print(*matrix[i])
                # print(flag)

elif input_2 == 'D':
    for j in range(4):
        flag = 0
        for i in range(2, -1, -1): 
            # duyet tung cot 1 den 3 vi cot 0 da co dk kiem tra ben trong
            while i != 3:
                if i + 1 < 4 and i >= 0:
                    if matrix[i + 1][j] == matrix[i][j] == '0':
                        break
                    if matrix[i + 1][j] == '0' or matrix[i + 1][j] == matrix[i][j] and flag == 0:
                        if matrix[i + 1][j] == matrix[i][j]:
                            flag = 1
                        matrix[i + 1][j] = str(int(matrix[i + 1][j]) + int(matrix[i][j]))
                        matrix[i][j] = '0'
                i += 1
    for row in matrix:
        print(*row)
        
    exit()

elif input_2 == 'U':
    for j in range(4):
        flag = 0
        for i in range(1, 3): 
            # duyet tung cot 1 den 3 vi cot 0 da co dk kiem tra ben trong
            while i != 3:
                if i - 1 >= 4 and i < 4:
                    if matrix[i - 1][j] == matrix[i - 1][j] == '0':
                        break
                    if matrix[i - 1][j] == '0' or matrix[i - 1][j] == matrix[i][j] and flag == 0:
                        if matrix[i - 1][j] == matrix[i][j]:
                            flag = 1
                        matrix[i - 1][j] = str(int(matrix[i - 1][j]) + int(matrix[i][j]))
                        matrix[i][j] = '0'
                i -= 1


for row in matrix:
    print(*row)
        

