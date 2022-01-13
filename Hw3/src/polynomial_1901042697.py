

def foo(a:list, x:int,n:int):
	if n == 0:
		return 0
	# print(f"{a[n-1]} * {pow(x,n)} = {a[n-1] * pow(x,n)}" )
	return a[n-1] * pow(x,n) + foo(a, x , n-1);

ll = [1,2,3]
num = 5
print(foo(ll, num, len(ll)))













