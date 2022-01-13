import math
stops = ["A","B","C","D","E","F","G"]
dictStopsVal = {"A":3, "B":-5, "C":2, "D":11, "E":-8, "F":9, "G":-5}

# 5 A
def findAllSubSet():
	subsets = []
	for i,stop in enumerate(stops):
		tmp = [stop]
		subsets.append(tmp.copy())
		for _next in stops[i+1:]:
			tmp.append(_next)
			subsets.append(tmp.copy())
	return subsets

def calculateProfit(_subset):
	profit = 0.0
	for stop in _subset:
		profit = profit + dictStopsVal[stop]

	return profit

def findMostProfibleCluster(_subsets):
	profit = -math.inf
	mostProfiableCluster = []
	
	for _subset in _subsets:
		cProfit = calculateProfit(_subset)
		if cProfit > profit:
			profit = cProfit
			mostProfiableCluster = _subset

	return mostProfiableCluster


subsets = findAllSubSet()
mostPro = findMostProfibleCluster(subsets)

print(f"PART A: {mostPro}")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
print("===================================")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def maxValue(ll):
	_max = -math.inf 
	_stop = ""
	for stop in ll:
		if dictStopsVal[stop] > _max:
			_max = dictStopsVal[stop]
			_stop = stop

	return _max,_stop


_maxVal = -math.inf
_stop = ""
_maxSet = []
def maxCluster(ll, pt1, pt2, tmp_max):
	global _maxSet,_maxVal, _stop

	if len(ll) < pt1 or len(ll) < pt2:
		return
	if calculateProfit(ll[pt1:pt2]) > tmp_max:
		tmp_max = calculateProfit(ll[pt1:pt2])
		_maxSet = ll[pt1:pt2]
		_maxVal,_stop = maxValue(ll[pt1:pt2])
	maxCluster(ll, pt1+1,pt2,tmp_max)
	
	maxCluster(ll, pt1, pt2+1, tmp_max)



maxCluster(stops,0,1,-1)

print("PART B")
print(f"maxCluster : {_maxSet}")
print(f"maxStop : {_stop} {_maxVal} ")
