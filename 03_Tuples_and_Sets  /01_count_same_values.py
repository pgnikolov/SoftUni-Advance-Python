nums = [float(el) for el in input().split()]

num_count_dict = {}

for num in nums:
    if num not in num_count_dict:
        num_count_dict[num] = 0
    num_count_dict[num] += 1

for num in num_count_dict:
    print(f"{num} - {num_count_dict[num]} times")