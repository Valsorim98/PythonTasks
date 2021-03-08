n = int(input())

sum1 = 0
sum2 = 0

for i in range(0, n):
    num1 = int(input())
    sum1 += num1

for j in range(0, n):
    num2 = int(input())
    sum2 += num2

diff = abs(sum1 - sum2)

if sum1 == sum2:
    print(f"Yes, sum = {sum1}")
elif sum1 != sum2:
    print(f"No, diff = {diff}")