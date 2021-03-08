name = str(input())

counter = 0
sum_grade = 0
fails = 0

while counter < 12:
    grade = float(input())
    if grade >= 4:
        counter += 1
        fails = 0
    elif grade < 4:
        fails += 1
        if fails == 2:
            print(f"{name} has been excluded at {counter + 1} grade")
            break
    sum_grade += grade
    av_grade = sum_grade / counter

if counter == 12:
    print(f"{name} graduated. Average grade: {av_grade:.2f}")