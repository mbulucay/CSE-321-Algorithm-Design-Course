def count(message:list, l, m, r):

	left  = message[l:m+1]
	right = message[m+1:r+1]

	i = j = counter = 0
	k = l

	while( i < len(left) and j < len(right)):
		if left[i] <= right[j]:
			message[k] = left[i]
			i = i + 1
		else:
			message[k] = right[j]
			j = j + 1
			count = (m+1) - (l+i)
			counter = counter + count

		k = k + 1

	while (i < len(left)):
		message[k] = left[i]
		i = i + 1
		k = k + 1

	while (j < len(right)):
		message[k] = right[j]
		j = j + 1
		k = k + 1

	return counter


def divide(message:list, low:int, high:int):
	if low >= high:
		return 0

	mid = low + (high - low) // 2 

	left = divide(message,low,mid)
	right = divide(message,mid+1, high)

	merge = count(message, low, mid, high)

	return left + merge + right


def rop(message:list):
	return divide(message,0,len(message)-1)

#ll = [10, 3, 4, 2, 5, 7, 9, 11]
ll = [12,11,13,5,6,7]

print(rop(ll))







