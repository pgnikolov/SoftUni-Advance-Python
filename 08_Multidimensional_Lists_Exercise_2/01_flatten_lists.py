sub_lists = input().split('|')
sub_lists = sub_lists[::-1]
result = []
for sub_list in sub_lists:
    numbers = sub_list.split()
    result.extend(numbers)

print(" ".join(result))
