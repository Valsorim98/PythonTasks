deposit_sum = float(input())
deposit_month = int(input())
rate_per_year = float(input())

rate_for_year = deposit_sum * rate_per_year / 100
rate_for_month = rate_for_year / 12
total = deposit_sum + (deposit_month * (rate_for_month))
print (total)