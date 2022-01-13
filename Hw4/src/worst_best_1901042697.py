
from random import sample

def max_min_rate(rateList:list):

	if(len(rateList) > 1):

		rightSide = rateList[:len(rateList)//2]
		leftSide  = rateList[len(rateList)//2:]

		minRight, maxRight = max_min_rate(rightSide)
		minLeft , maxLeft = max_min_rate(leftSide)

		return min(minLeft,minRight),max(maxLeft, maxRight)
	else:	
		return rateList[0], rateList[0]

ll = list(sample(range(20,80),25))
print(f"rate list = {ll}")

_min, _max = max_min_rate(ll)

print(f"min rate = {_min} \nmax rate {_max}")


