import fileinput, re
from collections import deque

mat = []
for l in fileinput.input():
	mat.append([x for x in l.strip()])
for y in range(len(mat)):
	for x in range(len(mat[0])):
		if mat[y][x] == 'S':
			pos = [(x,y)]
for step in range(1,64+1):
	npos = []
	for x,y in pos:
		for nx,ny in ((x,y+1),(x,y-1),(x+1,y),(x-1,y)):
			if nx>=0 and ny>=0 and nx<len(mat[0]) and ny<len(mat) and mat[ny][nx] != '#':
				npos.append((nx,ny))
	npos = list(set(npos))
	pos = npos
print(len(npos))
