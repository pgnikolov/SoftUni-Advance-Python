from collections import deque

def increment_time(current_time):
    current_time[2] += 1
    if current_time[2] == 60:
        current_time[2] = 0
        current_time[1] += 1
        if current_time[1] == 60:
            current_time[1] = 0
            current_time[0] += 1
            if current_time[0] == 24:
                current_time[0] = 0
    return current_time

def check_free_robots(working_robots):
    newly_free_robots = deque([])
    for _ in range(len(working_robots)):
        robot = working_robots.popleft()
        remaining_time = robot[2]
        if remaining_time == 0:
            robot.pop()
            newly_free_robots.append(robot)
        else:
            working_robots.append(robot)
    return newly_free_robots, working_robots

def update_working_robots(working_robots):
    for _ in range(len(working_robots)):
        robot = working_robots.popleft()
        robot[2] -= 1
        working_robots.append(robot)
    return working_robots

robot_data = [robot.split('-') for robot in input().split(";")]
robot_order = [robot[0] for robot in robot_data]

available_robots = deque(robot_data)
busy_robots = deque([])

start_time = [int(x) for x in input().split(":")]
current_time = start_time

production_line = deque([])
while True:
    product = input()
    if product == "End":
        break
    production_line.append(product)

while production_line:
    current_time = increment_time(start_time)
    next_product = production_line.popleft()

    if available_robots:
        active_robot = available_robots.popleft()
        print(f"{active_robot[0]} - {next_product} "
              f"[{current_time[0]:02d}:{current_time[1]:02d}:{current_time[2]:02d}]")
        processing_time = int(active_robot[1])
        active_robot.append(processing_time)
        busy_robots.append(active_robot)

    else:
        production_line.append(next_product)

    busy_robots = update_working_robots(busy_robots)

    free_robots, busy_robots = check_free_robots(busy_robots)

    if free_robots:
        reordered_robots = []
        all_robots_available = available_robots + free_robots
        for robot_name in robot_order:
            for _ in range(len(all_robots_available)):
                robot = all_robots_available.popleft()
                if robot[0] == robot_name:
                    reordered_robots.append(robot)
                else:
                    all_robots_available.append(robot)
        available_robots = deque(reordered_robots)
