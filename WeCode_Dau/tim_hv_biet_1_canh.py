A = input().split()

B = input().split()

x1 = int(A[0])
x2 = int(B[0])
y1 = int(A[1])
y2 = int(B[1])

# tim ra chi phuong
AB_1 = x2 - x1
AB_2 = y2 - y1

#  hai vector vuong goc
AB_square_1 = [AB_2, AB_1]
AB_square_2 = [AB_2, - AB_1]

# first square
C1 = [x1 - AB_2, y1+ AB_1]
D1 = [x2 - AB_2, y2 + AB_1]

# second square
C2 = [x1 + AB_2, y1 - AB_1]
D2 = [x2 + AB_2, y2 - AB_1]

print(f"({x1}, {y1}) ({C1[0]}, {C1[1]}) ({D1[0]}, {D1[1]}) ({x2}, {y2})")
print(f"({x1}, {y1}) ({x2}, {y2}) ({D2[0]}, {D2[1]}) ({C2[0]}, {C2[1]})")  


