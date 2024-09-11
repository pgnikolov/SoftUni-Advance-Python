from collections import deque

price_per_bullet = int(input())
barrel_capacity = int(input())
bullet_list = [int(num) for num in input().split()]
lock_queue = deque([int(num) for num in input().split()])
reward_value = int(input())
remaining_bullets = len(bullet_list)
barrel = deque([bullet_list.pop() for _ in range(barrel_capacity) if bullet_list])
total_cost = 0

while remaining_bullets > 0 and lock_queue:

    current_lock = lock_queue.popleft()
    current_bullet = barrel.popleft()
    remaining_bullets -= 1
    total_cost += price_per_bullet

    if current_bullet <= current_lock:
        print("Bang!")
    else:
        lock_queue.appendleft(current_lock)
        print("Ping!")

    if not barrel and bullet_list:
        barrel = deque([bullet_list.pop() for _ in range(barrel_capacity) if bullet_list])
        print("Reloading!")

if lock_queue:
    print(f"Couldn't get through. Locks left: {len(lock_queue)}")
else:
    print(f"{remaining_bullets} bullets left. Earned ${reward_value - total_cost}")
