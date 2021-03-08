space = float(input())
price = space * 7.61
discount = float(price) * 0.18

total = price - discount
print ("The final price is: " + str(round(total, 2)) + " lv.")
print ("The discount is: " + str(round(discount, 2)) + " lv.")