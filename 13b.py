import fileinput

def reflec(mat, smudges):
	#print(mat)
	for h in range(1, len(mat)):
		pairs = zip(reversed(mat[:h]), mat[h:])
		diffs = len([0 for a,b in pairs for x,y in zip(a,b) if x != y])
		if diffs == smudges:
			#print("HORZ", h)
			return 100*h

	for v in range(1, len(mat[0])):
		pairs = zip(reversed([[mat[x][y] for x in range(len(mat))] for y in range(v)]),
			[[mat[x][y] for x in range(len(mat))] for y in range(v, len(mat[0]))])
		diffs = len([0 for a,b in pairs for x,y in zip(a,b) if x != y])
		if diffs == smudges:
			#print("VERT", v)
			return v
	assert False

tot = 0
mat = []
for l in fileinput.input():
	l = l.strip()
	if len(l) == 0:
		tot += reflec(mat, 1)
		mat = []
	else:
		mat.append(l.strip())
print(tot)
