
# em quen cach tim ra so nguyen to nen em xem tren geekforgeek va dieu chinh
# 1 ham rieng trong code cua minh 
# em co check tren chatgpt de kiem tra ki dieu kien cua ham 
def is_prime(number):
    if number == 1:
        return False
    elif number % 2 == 0:
        return False

    for i in range (3, (number//2)+1, 2):
        if number % i == 0:
            return False
    return True

input_data = int(input())
count = 0

for number_1 in range (input_data//2 +1):
    number_2 = input_data - number_1
    if is_prime(number_1) and is_prime(number_2):
        count += 1
    
print(count)

