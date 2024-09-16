guests_amount = int(input())
guests = set()

for _ in range(guests_amount):
    code = input()
    if len(code) == 8:
        guests.add(code)
    else:
        continue

command = input()
while command != "END":
    if command in guests:
        guests.remove(command)
    else:
        continue
    command = input()

missed_party = list(guests)
missed_party.sort()

print(len(missed_party))
print("\n".join(missed_party))
