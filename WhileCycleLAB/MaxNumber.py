import sys

command = input()

max = -sys.maxsize

while command != "Stop":
    num = int(command)
    if num > max:
        max = num
    command = input()

print(max)