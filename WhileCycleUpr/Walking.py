command = input()

steps = 0

while command != "":
    if command != "Going home":
        steps += int(command)
    if steps >= 10000:
        goal = steps - 10000
        print("Goal reached! Good job!")
        print(f"{goal} steps over the goal!")
        break
    if command == "Going home":
        command = input()
        steps += int(command)
        if steps < 10000:
            goal = abs(steps - 10000)
            print(f"{goal} more steps to reach goal.")
            break
        elif steps >= 10000:
            goal = steps - 10000
            print("Goal reached! Good job!")
            print(f"{goal} steps over the goal!")
            break
    command = input()