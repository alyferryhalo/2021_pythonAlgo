# selection sort

def find_smallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for num in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index
	
def selection_sort(arr):
	new_arr = []
	for num in range(len(arr)):
		smallest = find_smallest(arr)
		new_arr.append(arr.pop(smallest))
	return new_arr
	
print(selection_sort([5, 7, 1, 4, 10, 222]))
