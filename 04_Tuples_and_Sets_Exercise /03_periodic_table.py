lines = int(input())

chemical_elements = []

for _ in range(lines):
    chemical_elements.append(input().split())

flat_list = [item for sublist in chemical_elements for item in sublist]
chemical_set = set(flat_list)
print("\n".join(chemical_set))
