from collections import deque

water_qnt = int(input())
people = deque()
command = input()

while command != "Start":
    people.append(command)
    command = input()

command = input()

while command != "End":
    info = command.split()
    if info[0] == "refill":
        water_qnt += int(info[1])
    elif int(info[0]) > water_qnt:
        print(f"{people.popleft()} must wait")
    else:
        water_qnt -= int(info[0])
        print(f"{people.popleft()} got water")
    command = input()

print(f"{water_qnt} liters left")
