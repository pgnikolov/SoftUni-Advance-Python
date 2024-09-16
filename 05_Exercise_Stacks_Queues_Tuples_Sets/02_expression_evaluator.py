from collections import deque
from math import floor

symbols_queue = deque(input().split())

working_numbers = deque([])

while len(symbols_queue) > 0:
    current_symbol = symbols_queue.popleft()
    if current_symbol.lstrip("-").isdigit():
        working_numbers.append(int(current_symbol))
        continue

    while len(working_numbers) > 1:
        num1 = working_numbers.popleft()
        num2 = working_numbers.popleft()
        result = 0
        if current_symbol == "+":
            result = num1 + num2
        elif current_symbol == "-":
            result = num1 - num2
        elif current_symbol == "*":
            result = num1 * num2
        elif current_symbol == "/":
            result = floor(num1 / num2)

        working_numbers.appendleft(result)
    new_number = str(working_numbers.popleft())
    symbols_queue.appendleft(new_number)

print(*working_numbers)
