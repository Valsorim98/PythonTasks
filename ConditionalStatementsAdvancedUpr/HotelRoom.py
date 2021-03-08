month = str(input())
days = int(input())

if 7 < days <= 14:
    if month == "May" or month == "October":
        price_stud = (days * 50) * 0.95
    elif month == "June" or month == "September":
        price_stud = days * 75.2
    elif month == "July" or month == "August":
        price_stud = days * 76


elif days <= 7:
    if month == "May" or month == "October":
        price_stud = days * 50
    elif month == "June" or month == "September":
        price_stud = days * 75.2
    elif month == "July" or month == "August":
        price_stud = days * 76

elif days > 14:
    if month == "May" or month == "October":
        price_stud = (days * 50) * 0.7
    elif month == "June" or month == "September":
        price_stud = (days * 75.2) * 0.8
    elif month == "July" or month == "August":
        price_stud = days * 76

if days > 14:
    if month == "May" or month == "October":
        price_ap = (days * 65) * 0.9
    elif month == "June" or month == "September":
        price_ap = (days * 68.7) * 0.9
    elif month == "July" or month == "August":
        price_ap = (days * 77) * 0.9
elif days <= 14:
    if month == "May" or month == "October":
        price_ap = days * 65
    elif month == "June" or month == "September":
        price_ap = days * 68.7
    elif month == "July" or month == "August":
        price_ap = days * 77

print(f"Apartment: {price_ap:.2f} lv.")
print(f"Studio: {price_stud:.2f} lv.")