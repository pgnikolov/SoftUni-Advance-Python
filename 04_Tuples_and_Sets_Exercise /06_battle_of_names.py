import math
lines = int(input())

odds = set()
evens = set()

for i in range(1, lines + 1):
    name_value = sum([ord(i) for i in input()])
    name_line = math.floor(name_value / i)
    if name_line % 2 != 0:
        odds.add(name_line)
    else:
        evens.add(name_line)

if sum(odds) == sum(evens):
    print(", ".join(map(str, odds.union(evens))))
elif sum(odds) > sum(evens):
    print(", ".join(map(str, odds.difference(evens))))
elif sum(evens) > sum(odds):
    print(", ".join(map(str, odds.symmetric_difference(evens))))
