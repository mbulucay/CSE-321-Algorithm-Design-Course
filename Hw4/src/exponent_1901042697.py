
def div_and_conq(a:int, n:int):
	if n == 0:
		return 1
	else:
		m = div_and_conq(a, n//2)
		if n % 2 == 0:
			return m * m
		else:
			return m * m * a


def brute_force(a:int, n:int):
	r = 1
	for i in range(n):
		r = r * a
	return r


print(div_and_conq(2,4))

print(brute_force(2,3))


