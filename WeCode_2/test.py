def reverse_num(number: str) -> str:
    return number[::-1]

def is_palindrome(number: str) -> bool:
    return number == number[::-1]

def check_lychrel_candidate(input_data: str):
    max_iterations = 10000
    max_length = 15000
    number_list = [input_data]  # To store all results

    for i in range(max_iterations):
        reverse = reverse_num(input_data)
        input_data = str(int(input_data) + int(reverse))  # Reverse-and-add process
        number_list.append(input_data)

        # Check if a palindrome is formed
        if is_palindrome(input_data):
            print("NO")
            print("\n".join(number_list))
            return

        # Check if the number exceeds 15,000 digits
        if len(input_data) > max_length:
            break

    # If no palindrome was formed after 10,000 iterations or number exceeds 15,000 digits
    print("YES")
    print(i + 1)
    print(input_data)

# Input handling
import sys
import time
# Start time tracking
start_time = time.time()
input_data = sys.stdin.readline().strip()  # Reading the input
check_lychrel_candidate(input_data)
# End time tracking
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
