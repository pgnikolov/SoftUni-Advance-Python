from collections import deque


def process_crossing(green_duration: int, free_duration: int, cars: deque, passed_count: int):
    current_car = deque([])
    last_car = ""

    for _ in range(green_duration):
        if not current_car and cars:
            passed_count += 1
            last_car = cars.popleft()
            current_car = deque([char for char in last_car])
        if current_car:
            current_car.popleft()

    for _ in range(free_duration):
        if current_car:
            current_car.popleft()

    if current_car:
        print("A crash happened!")
        print(f"{last_car} was hit at {current_car[0]}.")
        quit()

    return cars, passed_count


green_time = int(input())
pass_time = int(input())
car_line = deque([])
cars_passed = 0

while True:
    command = input()

    if command == "END":
        print("Everyone is safe.")
        print(f"{cars_passed} total cars passed the crossroads.")
        break

    elif command == "green":
        car_line, cars_passed = process_crossing(green_time, pass_time, car_line, cars_passed)

    else:
        car_line.append(command)
