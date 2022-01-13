import random


gifts = list(range(1,6))
boxes = list(range(1,6))

random.shuffle(gifts)
random.shuffle(boxes)

print(f"boxes list : {boxes}")
print(f"gifts list (before sorted according to the boxes): {gifts}")

def partition(boxes:list, gifts:list, start:int, end:int):

	while 0 <= end and gifts[end] != boxes[start]:
		end = end - 1 

	gifts[start], gifts[end] = gifts[end], gifts[start]

	return end


def quick(boxes:list, gifts:list, start:int, end:int):

	if(start <= end):
		p = partition(boxes, gifts, start, end)
		quick(boxes, gifts, start, p - 1)
		quick(boxes, gifts, p + 1 , end)

	return gifts


gifts = quick(boxes,gifts,0,len(gifts)-1)


print(f"gifts list (after sorted according to the boxes): {gifts}")











