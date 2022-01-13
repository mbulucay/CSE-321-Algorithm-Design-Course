from math import floor, ceil, log

def min(length:int):
	return floor(log(length,2))


def minCutDivideAndConq(length:int):
	if(length == 1):
		return 0
	return   1 + minCutDivideAndConq(ceil(length / 2))


def minCutDecreaseAndConq(length:int, start = 1):
	if(1 >= length):
		return 0;
	return 1 + minCutDecreaseAndConq( length - start, start*2)


for l in range(1,34):
	print(f"length = {l} minimum cut = {minCutDecreaseAndConq(l)}")


