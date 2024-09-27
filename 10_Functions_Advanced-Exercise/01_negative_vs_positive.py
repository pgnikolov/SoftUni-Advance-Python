nums = [int(char) for char in input().split()]
positive = [x for x in nums if x >= 0]
negative = [x for x in nums if x < 0]

print(sum(negative))
print(sum(positive))
if abs(sum(positive)) > abs(sum(negative)):
    print('The positives are stronger than the negatives')
else:
    print('The negatives are stronger than the positives')
