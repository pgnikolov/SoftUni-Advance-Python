from collections import deque

material_boxes = [int(x) for x in input().split()]
magic_queue = deque(int(x) for x in input().split())

crafted_presents = {
    "Bicycle": [0, 400],
    "Doll": [0, 150],
    "Teddy bear": [0, 300],
    "Wooden train": [0, 250]
}

while material_boxes and magic_queue:
    current_material = material_boxes.pop()
    current_magic = magic_queue.popleft()

    if current_material == 0 and current_magic == 0:
        continue
    if current_material == 0:
        magic_queue.appendleft(current_magic)
        continue
    if current_magic == 0:
        material_boxes.append(current_material)
        continue

    operation_result = current_material * current_magic
    if operation_result < 0:
        new_material = current_material + current_magic
        material_boxes.append(new_material)

    else:
        gift_found = False
        for present, value in crafted_presents.items():
            _, required_magic = value
            if required_magic == operation_result:
                crafted_presents[present][0] += 1
                gift_found = True
                break
        if operation_result > 0 and not gift_found:
            material_boxes.append(current_material + 15)

if (crafted_presents["Bicycle"][0] >= 1 and crafted_presents["Teddy bear"][0] >= 1) or \
        (crafted_presents["Doll"][0] >= 1 and crafted_presents["Wooden train"][0] >= 1):
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if material_boxes:
    print(f"Materials left: {', '.join(str(x) for x in material_boxes[::-1])}")

if magic_queue:
    print(f"Magic left: {', '.join(str(x) for x in magic_queue)}")

for present, value in crafted_presents.items():
    crafted_count, _ = value
    if crafted_count >= 1:
        print(f"{present}: {crafted_count}")
