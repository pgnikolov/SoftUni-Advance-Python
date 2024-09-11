from collections import deque
food_qnt = int(input())

orders_food = deque(int(num) for num in input().split())
print(max(orders_food))

while True:
	if orders_food and orders_food[0] <= food_qnt:
		food_qnt -= orders_food.popleft()
	else:
		break

if orders_food:
	print(f"Orders left: {' '.join(map(str, orders_food))}")
else:
	print("Orders complete")
