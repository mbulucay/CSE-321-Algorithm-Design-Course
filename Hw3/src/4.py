
import math

def calTwoPointDist(p1:tuple, p2:tuple):
	dist = 0.0
	for c1,c2 in zip(p1,p2):
		dist = dist + pow(c1-c2,2)
	return math.sqrt(dist)



def minDist(points:list):
	minDist = math.inf;
	for i,p1 in enumerate(points):
		for p2 in points[i+1:]:
			if calTwoPointDist(p1,p2) < minDist:
				minDist = calTwoPointDist(p1,p2)
		
	print(minDist)
	

p1 = (1,2,1)
p2 = (1,5,2)
p3 = (5,5,5)
p4 = (-1,7,9)

points = [p1,p2,p3,p4]

minDist(points)




