# em co tham khao geekforgeek cho bai toan nay a 

def check_valid_IP(input_data):
    split_data = input_data.split('.')

    for i in split_data:
        if not i.isdigit():
            return False

        if int(i) < 0 or int(i) > 255:
            return False

        if len(i) > 1 and i[0] == '0':
            return False

    return True

# em co tham khao chatgpt de hoan thien backtracking
# em biet co phuong phap giai 3 dong for nhung em muon on lai backtracking a

def trying(input_data, dot, start = 0, current=""):  
    if dot == 0:
        current += input_data[start:]
        if check_valid_IP(current):
            print(current)
        return
    
    for i in range(start, len(input_data)):
        if i < len(input_data) - 1:
            
            next_current = current + input_data[start:i+1] + '.'
        #    why i cant use current but instead use next_current cause changing the current maybe affect the other branch of recursive func make it complicated to maintain
            trying(input_data, dot - 1, i + 1, next_current)


input_data = input()
dot = 3
trying(input_data, dot)

