lines = int(input())
parking = set()

for _ in range(lines):
    info = input().split(", ")
    direction = info[0]
    car_plate = info[1]
    if direction == "IN":
        parking.add(car_plate)
    elif direction == "OUT":
        parking.remove(car_plate)

if parking:
    print("\n".join(parking))
else:
    print("Parking Lot is Empty")
