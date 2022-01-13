from itertools import permutations

c = 0

def partition(start, end, array):
	global c
	pivot_index = start 
	pivot = array[pivot_index]
      
	while start < end:
          
		while start < len(array) and array[start] <= pivot:
			start += 1
		while array[end] > pivot:
			end -= 1

		if(start < end):
			c = c + 1
			array[start], array[end] = array[end], array[start]

	array[end], array[pivot_index] = array[pivot_index], array[end]
	c = c + 1
	return end
      
def quick_sort(start:int, end:int, array:list):
    
    if (start < end):
          
        p = partition(start, end, array)
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)


array = [1,2,3,4,5,6,7,8]
p = permutations(array)

maxc = 0
maxarr = []

for array in p:
	array = list(array)
	quick_sort(0, len(array) - 1, array)
	print(f'Sorted array: {array}   swap: {c}')
	if c > maxc:
		maxc = c
		maxarr = array
	c = 0

print(f'result array: {maxarr}   swap: {maxc}')