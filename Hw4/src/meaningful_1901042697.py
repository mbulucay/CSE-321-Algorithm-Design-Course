from random import sample


def partition(nums, left, right):
    pivot = nums[right] 
    i = left
    for j in range(left, right): 
        if nums[j] > pivot: 
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    nums[right], nums[i] = nums[i], nums[right]
    return i


def quickSelect( nums, start, n, k):
	pos = partition(nums, start, n)
	if pos == k-1:
		return nums[pos]
	elif pos >= k:
		return quickSelect(nums, start, pos - 1, k)
	return quickSelect(nums, pos + 1, n, k)
    

def findKthLargest(nums, k):
    return quickSelect(nums, 0, len(nums)-1, k)
    
ll = list(sample(range(20,80),25))
print(f"rate list = {ll}")

kth = int(input("Enter the kth rate : "))

try:
	kth = findKthLargest(ll,len(ll) - kth + 1);
	print(f"kth rate = {kth} ")
except :
	print("Index out of length")
