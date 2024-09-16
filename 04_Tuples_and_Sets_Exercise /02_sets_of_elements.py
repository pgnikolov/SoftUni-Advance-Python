n, m = input().split()

set1 = set()
set2 = set()

for _ in range(int(n)):
    set1.add(input())

for _ in range(int(m)):
    set2.add(input())

intersection = set1.intersection(set2)

print("\n".join(intersection))
