# binary search

import random

num_list = []
for _ in range(100):
	num_list.append(random.randint(0,500))
# print(num_list)

num_list_sorted = num_list.sort()  # TimSort O(n log n)
# print(num_list_sorted)

def binary_search(number_list, number, left, right):
	if left > right:
		return -1
	middle = (left + right) // 2
	if number == numbers_list[middle]:
		return middle
	elif number < numbers_list[middle]:
		return binary_search(number_list, number, left, middle-1)
	else:
		return binary_search(number_list, number, middle+1, right)
  
print(binary_search(num_list_sorted, 90, 0, len(num_list_sorted)-1))
