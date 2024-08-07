from collections import deque

names = deque(input().split())
turs = int(input())

while len(names) > 1:
    for i in range(1, turs + 1):
        if i == turs:
            print(f"Removed {names.popleft()}")
            continue
        names.rotate(-1)

print(f"Last is {''.join(names)}")
