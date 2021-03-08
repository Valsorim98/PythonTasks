import sys

n = int(input())

max_num = -sys.maxsize
sum = 0

for i in range(n):
    num = int(input())
    sum += num
    if num > max_num:
        max_num = num

sum -= max_num
diff = abs(max_num - sum)

if max_num == sum:
    print("Yes")
    print(f"Sum = {sum}")
elif max_num != sum:
    print("No")
    print(f"Diff = {diff}")