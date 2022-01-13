 
import math
stops = ["A","B","C","D","E","F","G"]
dictStopsVal = {"A":3, "B":-5, "C":2, "D":11, "E":-8, "F":9, "G":-5}


ansArr = [0,0,0,0,0,0,0,0]
_max = -math.inf
for i,stop in enumerate(stops):
    ansArr[i] = max(dictStopsVal[stop] + ansArr[i-1], ansArr[i])
    if ansArr[i] > _max:
        _max = ansArr[i]

print(_max)

print(ansArr)

l = [3,-5,2,11,-8,-5]

for i in range(len(l)):
    ansArr [i] = max(l[i] + ansArr[i-1], ansArr[i])
    if ansArr[i] > _max:
        _max = ansArr[i]

print(ansArr)


