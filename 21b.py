import fileinput, re
from collections import deque

mat = []
for l in fileinput.input():
	mat.append(l.strip())
MX,MY = len(mat[0]), len(mat)
print("sizes", MX, MY)
for y in range(len(mat)):
	for x in range(len(mat[0])):
		if mat[y][x] == 'S': pos = [(x,y)]

def cache(pos):
	counts = [len(pos)]
	save = set([tuple(sorted(pos))])
	for step in range(1,1000):
		npos = []
		for x,y in pos:
			for nx,ny in ((x,y+1),(x,y-1),(x+1,y),(x-1,y)):
				if nx>=0 and ny>=0 and nx<len(mat[0]) and ny<len(mat):
					if mat[ny][nx] != '#': npos.append((nx,ny))
		pos = list(set(npos))
		hsh = tuple(sorted(pos))
		if hsh in save: break
		save.add(hsh)
		counts.append(len(pos))
	return counts
def grok(counts, step):
	if step < len(counts): return counts[step]
	return counts[-2] if (step - len(counts))%2 == 0 else counts[-1]

central = cache(pos)
edges = [cache([(MX-1,MY//2)]), cache([(0,MY//2)]), cache([(MX//2,MY-1)]), cache([(MX//2,0)])]
corners = [cache([(0,0)]), cache([(0,MY-1)]), cache([(MX-1,0)]), cache([(MX-1,MY-1)])]

target = 26501365
tot = grok(central, target)
for i in range(MX//2+1, target+1, MX):
	for e in edges:
		tot += grok(e, target-i)
mult = 1
for i in range(MX+1, target+1, MX):
	for c in corners:
		tot += mult * grok(c, target-i)
	mult += 1
print(tot)
