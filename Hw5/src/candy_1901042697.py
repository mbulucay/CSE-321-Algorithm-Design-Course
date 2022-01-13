
prices = [1, 5, 8, 9, 10, 17, 17, 20]
lengths = [1, 2, 3, 4, 5, 6, 7, 8]
size = len(prices)
ansprices = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def cutRod(n):
	global ansprices,prices
	for i in range(1, n+1):
		max_val = -1
		for j in range(i):
			max_val = max(max_val, prices[j] + ansprices[i-j-1])
		ansprices[i] = max_val

	return ansprices[n]

print(f"Max Obtained values: {cutRod(size)}")
print(ansprices)
