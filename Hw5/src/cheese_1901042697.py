from operator import truediv

W = 15
objects = [1, 2, 3, 4, 5, 6, 7]
prices = [10, 5, 15, 7, 6, 18, 3]
weights = [2, 3, 5, 7, 1, 4, 1]
getList = [0, 0, 0, 0, 0, 0, 0]


result = list(zip(range(len(objects)),map(lambda x,y: x/y,prices, weights)))
result.sort(key = lambda x: x[1], reverse=True) 

for i,value in result:
	if W > 0:
		if W > weights[i]:
			getList[i] = 1
		else:
			getList[i] = round(W / weights[i], 2)
		W = W - weights[i]


print(result)
print(getList)

