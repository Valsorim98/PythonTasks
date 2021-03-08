import sys

n = int(input())
if n == 0:
    print("OddSum=0.00,")
    print("OddMin=No,")
    print("OddMax=No,")
    print("EvenSum=0.00,")
    print("EvenMin=No,")
    print("EvenMax=No")
    exit()

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

for i in range(1, n + 1):
    num = float(input())
    if i % 2 == 1:
        odd_sum += num
        if num < odd_min and num > odd_max:
            odd_min = num
            odd_max = num
        elif num < odd_min:
            odd_min = num
        elif num > odd_max:
            odd_max = num
    elif i % 2 == 0:
        even_sum += num
        if num < even_min and num > even_max:
            even_min = num
            even_max = num
        elif num < even_min:
            even_min = num
        elif num > even_max:
            even_max = num

print(f"OddSum={odd_sum:.2f},")
if i >= 1:
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
elif i < 1:
    print("OddMin=No,")
    print("OddMax=No,")

print(f"EvenSum={even_sum:.2f},")
if i >= 2:
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
elif i < 2:
    print("EvenMin=No,")
    print("EvenMax=No")