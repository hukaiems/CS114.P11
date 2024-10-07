import re 
import sys

pattern = r"^((\d[A-F]|[A-F]\d|\d\d|[A-F][A-F])(-)){5}(\d[A-F]|[A-F]\d|\d\d|[A-F][A-F]){1}$"

while True:
    input_data = sys.stdin.readline().strip()
    if input_data == '.':
        break
    
    if re.match(pattern, input_data):
        print("true")
    else:
        print("false")

