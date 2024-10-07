# input_data = str(input()).split()
# em co xem them y tuong cua ban Le Minh Nhat  MSSV: 22521060 khi con 
# test case 8 va 9 em khong giai quyet duoc a
# thay doi cua em la em doi thanh while True
# them vao phan nhap input readline() de doc tung dong thay vi doc tat ca a

import sys
list = set()

while True:
    input_data = sys.stdin.readline().strip().split()

    if input_data[0] == '0':
        break

    first_number = input_data[0]

    if first_number == '1':
        list.add(input_data[1])
            
    if first_number ==  '2':
        if input_data[1] in list:
            print(1)
        else:
            print(0)
    # em hoc duoc remove de xoa khoi list
    #em tim duoc them discard() de khong raise error khi xoa  set
    if first_number ==  '3':
        list.discard(input_data[1])

