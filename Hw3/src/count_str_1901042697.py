
string = "TXZXXJZWX"
start  = 'X'
end = 'Z'
counter = 0

for x,_start in enumerate(string):
	if _start == start and end in string[x:]: 
		for y, _end in enumerate(string[x:]):
			print(_end, end='')
			if end == _end:
				counter = counter + 1
				break
		print("")

print(f"Counter : {counter}")







