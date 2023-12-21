import fileinput

S = '-'
tr = {
	'|': ([(1,0), [(0,1)], [(0,-1)]],	[(-1,0), [(0,-1)], [(0,1)]]),
	'-': ([(0,1), [(-1,0)], [(1,0)]],	[(0,-1), [(1,0)], [(-1,0)]]),
	'L': ([(-1,0), [(0,-1),(1,0)], [(-1,1)]],	[(0,1), [(-1,1)], [(0,-1),(1,0)]]),
	'J': ([(-1,0), [(-1,-1)], [(1,0),(0,1)]],	[(0,-1), [(1,0),(0,1)], [(-1,-1)]]),
	'7': ([(1,0), [(-1,0),(0,1)], [(1,-1)]],	[(0,-1), [(1,-1)], [(-1,0),(0,1)]]),
	'F': ([(1,0), [(1,1)], [(-1,0),(0,-1)]],	[(0,1), [(-1,0),(0,-1)], [(1,1)]]),
}
grid = [[x for x in l.strip()] for l in fileinput.input()]
seen = [[0 for x in y] for y in grid]
for i in range(len(grid)):
	for j in range(len(grid[0])):
		if grid[i][j] == 'S':
			grid[i][j] = S
			seen[i][j] = 1
			a,b = tr[S][0][0]
			seen[i+a][j+b] = 1
			pos = (i+a, j+b)

def mark(pos, val):
	i,j = pos
	if i >= 0 and i < len(seen) and j >= 0 and j < len(seen[0]) and seen[i][j] == 0:
		seen[i][j] = val
		return True
	return False
while True:
	i,j = pos
	end = True
	for (a, b), l, r in tr[grid[i][j]]:
		if seen[i+a][j+b] <= 0:
			end = False
			seen[i+a][j+b] = 1
			pos = (i+a,j+b)
			for s,t in l: mark((i+s,j+t), -1)
			for s,t in r: mark((i+s,j+t), -2)
	if end: break

stack = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if seen[i][j] < 0]
while len(stack) > 0:
	i,j = stack.pop()
	for s in range(i-1,i+2):
		for t in range(j-1,j+2):
			if mark((s,t), seen[i][j]): stack.append((s,t))

print(sum([1 for y in seen for x in y if x == -2]))