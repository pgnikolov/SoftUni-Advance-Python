from collections import deque
import operator

bees = deque([int(num) for num in input().split()])
nectar_values = deque([int(num) for num in input().split()])
ops = deque([el for el in input().split()])
actions = {
    "+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul}
honey = 0

while True:
    if len(bees) == 0 or len(nectar_values) == 0:
        break
    if int(bees[0]) <= int(nectar_values[-1]):
        if int(nectar_values[-1]) == 0 and ops[0] == "/":
            bees.popleft()
            nectar_values.pop()
            ops.popleft()
            continue
        else:
            honey += abs(actions[ops[0]](bees[0], nectar_values[-1]))
            bees.popleft()
            nectar_values.pop()
            ops.popleft()
    else:
        nectar_values.pop()
        continue

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar_values:
    print(f"Nectar left: {', '.join(map(str, nectar_values))}")
