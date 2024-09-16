# first_set = set([int(el) for el in input().split()])
# second_set = set([int(el) for el in input().split()])
#
# # print(first_set)
# # print(second_set)
#
# number_of_commands = int(input())
#
# for _ in range(number_of_commands):
#     current_command_tokens = input().split()
#     real_command = ' '.join(current_command_tokens[:2])
#     # print(real_command)
#     current_set = set([int(el) for el in current_command_tokens[2:]])
#     # print(current_set)
#
#     if real_command == 'Add First':
#         first_set = first_set.union(current_set)
#     elif real_command == 'Add Second':
#         second_set = second_set.union(current_set)
#     elif real_command == 'Remove First':
#         first_set = first_set.difference(current_set)
#     elif real_command == 'Remove Second':
#         second_set = second_set.difference(current_set)
#     elif real_command == 'Check Subset':
#         is_subset = first_set.issubset(second_set) or second_set.issubset(first_set)
#         print(is_subset)
#
# first_set_as_sorted_list = sorted(list(first_set))
# second_set_as_sorted_list = sorted(list(second_set))
#
# print(*first_set_as_sorted_list, sep=", ")
# print(*second_set_as_sorted_list, sep=", ")

first_set = set([int(el) for el in input().split()])
second_set = set([int(el) for el in input().split()])

number_of_commands = int(input())

command_dict = {
    'Add First': lambda s: first_set.update(s),
    'Add Second': lambda s: second_set.update(s),
    'Remove First': lambda s: first_set.difference_update(s),
    'Remove Second': lambda s: second_set.difference_update(s),
    'Check Subset': lambda: print(first_set.issubset(second_set) or second_set.issubset(first_set))
}

for _ in range(number_of_commands):
    current_command_tokens = input().split()
    real_command = ' '.join(current_command_tokens[:2])
    if real_command == 'Check Subset':
        command_dict[real_command]()
    else:
        current_set = set([int(el) for el in current_command_tokens[2:]])
        command_dict[real_command](current_set)

first_set_as_sorted_list = sorted(list(first_set))
second_set_as_sorted_list = sorted(list(second_set))

print(*first_set_as_sorted_list, sep=", ")
print(*second_set_as_sorted_list, sep=", ")
