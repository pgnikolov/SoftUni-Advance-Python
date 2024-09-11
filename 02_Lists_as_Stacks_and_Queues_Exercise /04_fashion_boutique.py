box_clothes = [int(num) for num in input().split()]

rack_capacity = int(input())
total_racks = 1
current_rack = []

while box_clothes:
	if sum(current_rack) + box_clothes[-1] <= rack_capacity:
		current_rack.append(box_clothes.pop())
	else:
		current_rack.clear()
		total_racks += 1

print(total_racks)
