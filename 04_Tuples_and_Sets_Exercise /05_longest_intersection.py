lines = int(input())

longest = set()

for _ in range(lines):
    parts = input().split("-")
    part1 = [int(el) for el in parts[0].split(",")]
    part2 = [int(el) for el in parts[1].split(",")]
    part1set = set(n for n in range(part1[0], part1[1]+1))
    part2set = set(n for n in range(part2[0], part2[1] + 1))
    if len(longest) <= len(part1set.intersection(part2set)):
        longest = part1set.intersection(part2set)


print(f"Longest intersection is {list(longest)} with length {len(longest)}")
