import fileinput

def reflec(mat):
	#print(mat)
	for h in range(1, len(mat)):
		if all(a==b for a,b in zip(reversed(mat[:h]), mat[h:])):
			return 100*h
	for v in range(1, len(mat[0])):
		pairs = zip(reversed([[mat[x][y] for x in range(len(mat))] for y in range(v)]),
			[[mat[x][y] for x in range(len(mat))] for y in range(v, len(mat[0]))])
		if all(a==b for a,b in pairs):
			return v
	return 0

tot = 0
mat = []
for l in fileinput.input():
	l = l.strip()
	if len(l) == 0:
		tot += reflec(mat)
		mat = []
	else:
		mat.append(l.strip())
print(tot)
