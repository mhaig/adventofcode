import sys
from collections import Counter

location_ids = list(sys.stdin.readlines())

left_list = []
right_list = []

for ids in location_ids:
    left_list.append(int(ids.split()[0]))
    right_list.append(int(ids.split()[1]))

left_list.sort()
right_list.sort()

distance = 0
for ids in zip(left_list, right_list):
    distance += abs(ids[1] - ids[0])

print(f'Day 1 Part 1 Solution: {distance}')

# Convert right_list into a dictionary, counting duplicates.
right_dict = Counter(right_list)

similarity_score = 0
for ids in left_list:
    similarity_score += ids * right_dict.get(ids, 0)

print(f'Day 1 Part 1 Solution: {similarity_score}')
