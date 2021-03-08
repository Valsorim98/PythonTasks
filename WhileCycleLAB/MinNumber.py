import sys

command = input()

min = sys.maxsize

while command != "Stop":
    num = int(command)
    if num < min:
        min = num
    command = input()

print(min)