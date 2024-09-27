numbers = {}

while True:
    line = input()
    if line == "Search":
        break
    try:
        number_as_text = line
        number_as_int = int(input())
        numbers[number_as_text] = number_as_int
    except ValueError:
        print("The variable number must be an integer")

while True:
    line = input()
    if line == "Remove":
        break
    if line in numbers:
        print(numbers[line])
    else:
        print("Number does not exist in dictionary")

while True:
    line = input()
    if line == "End":
        break
    if line in numbers:
        del numbers[line]
    else:
        print("Number does not exist in dictionary")

print(numbers)
