from collections import deque

cups_capacity = deque([int(el) for el in input().split()])
filled_bottles = [int(el) for el in input().split()]

wasted_water = 0

while cups_capacity and filled_bottles:
    current_cup = cups_capacity.popleft()
    current_bottle = filled_bottles.pop()

    if current_cup <= current_bottle:
        wasted_water += current_bottle - current_cup

    else:
        current_cup -= current_bottle
        cups_capacity.appendleft(current_cup)

if filled_bottles:
    print(f"Bottles: {' '.join([str(el) for el in filled_bottles[::-1]])}")
elif cups_capacity:
    print(f"Cups: {' '.join([str(el) for el in cups_capacity])}")

print(f"Wasted litters of water: {wasted_water}")
