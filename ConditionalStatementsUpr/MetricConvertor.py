num = float(input())
unit_in = str(input())
unit_out = str(input())

final = 0

if unit_in == 'm' and unit_out == 'cm':
    num *= 100

elif unit_in == 'm' and unit_out == 'mm':
    num *= 1000

elif unit_in == 'cm' and unit_out == 'm':
    num /= 100

elif unit_in == 'cm' and unit_out == 'mm':
    num *= 10

elif unit_in == 'mm' and unit_out == 'm':
    num /= 1000

elif unit_in == 'mm' and unit_out == 'cm':
    num /= 10

print(f"{num:.3f}")