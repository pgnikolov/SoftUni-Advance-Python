from collections import deque

clients = deque()
command = input()
while command != "End":
    if command == "Paid":
        print("\n".join(clients))
        clients.clear()
    else:
        clients.append(command)

    command = input()

print(f"{len(clients)} people remaining.")
