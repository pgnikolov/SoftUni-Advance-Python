from collections import deque

lines = int(input())
stack = deque()

for _ in range(lines):
	action = input().split()
	if action[0] == '1':
		stack.append(int(action[1]))
	if len(stack) > 0:
		if action[0] == '2':
			stack.pop()
		elif action[0] == '3':
			print(max(stack))
		elif action[0] == '4':
			print(min(stack))

print(", ".join(map(str, reversed(stack))))
