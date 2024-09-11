from collections import deque

pumps = int(input())
pumps_values = []
journey = deque()
posible_journey = []
fuel_over = 0

for pumps in range(pumps):
	info = [int(el) for el in input().split()]
	pumps_values.append(info)
	journey.append(info[0] - info[1])

pump_jurney = deque(pumps_values.copy())

while not len(posible_journey) == len(pumps_values):
	for i in range(len(journey)):
		fuel_over += journey[i]
		if fuel_over < 0:
			fuel_over = 0
			journey.rotate(-1)
			pump_jurney.rotate(-1)
			posible_journey.clear()
			break
		posible_journey.append(pump_jurney[i])
	continue

print(pumps_values.index(posible_journey[0]))