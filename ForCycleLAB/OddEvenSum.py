n = int(input())

sum1 = 0
sum2 = 0

for i in range(0, n):
    if i % 2 == 0:
        num1 = int(input())
        sum1 += num1
    elif i % 2 != 0:
        num2 = int(input())
        sum2 += num2

diff = abs(sum1 - sum2)

if sum1 == sum2:
    print("Yes")
    print(f"Sum = {sum1}")
elif sum1 != sum2:
    print("No")
    print(f"Diff = {diff}")