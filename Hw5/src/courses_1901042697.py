def isCross(lec1:str, lec2:str):
	return (table[lec1]["start"] < table[lec2]["finish"] and table[lec1]["finish"] > table[lec2]["start"]) or (table[lec1]["start"] > table[lec2]["finish"] and table[lec1]["finish"] < table[lec2]["start"])


def isCrossList(lec,ll):
	for l in ll:
		if isCross(lec,l):
			return True
	return False

table = {"English":{"start": 1,"finish":2}, "Mathematics":{"start": 3,"finish":4},
			"Physics":{"start": 0,"finish":6}, "Chemistry":{"start": 5,"finish":7},
			"Biology":{"start": 8,"finish":9},"Geography":{"start": 5,"finish":9}}


diff = [("English" , table["English"]["finish"] - table["English"]["start"]),
		("Mathematics" , table["Mathematics"]["finish"] - table["Mathematics"]["start"]),
		("Physics" , table["Physics"]["finish"] - table["Physics"]["start"]),
		("Chemistry" , table["Chemistry"]["finish"] - table["Chemistry"]["start"]),
		("Biology" , table["Biology"]["finish"] - table["Biology"]["start"]),
		("Geography" , table["Geography"]["finish"] - table["Geography"]["start"])
]

diff.sort(key = lambda x: x[1]) 

OurLectures = []

for lec,time in diff:
	if isCrossList(lec,OurLectures) == False:
		OurLectures.append(lec)

print(OurLectures)
