bad_grades = int(input())

task_counter = 0
sum_grades = 0
fails = 0
last_task = ''

while fails < bad_grades:
    task = str(input())
    if task != "Enough":
        grade = int(input())
        task_counter += 1
        sum_grades += grade
        av_grade = sum_grades / task_counter
        last_task = task
    elif task == "Enough":
        print(f"Average score: {av_grade:.2f}")
        print(f"Number of problems: {task_counter}")
        print(f"Last problem: {last_task}")
    if grade <= 4:
        fails += 1

if fails == bad_grades:
    print(f"You need a break, {fails} poor grades.")