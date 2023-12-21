import fileinput

S = '-'
tr = {
	'|': ((1,0),(-1,0)),
	'-': ((0,1),(0,-1)),
	'L': ((-1,0),(0,1)),
	'J': ((-1,0),(0,-1)),
	'7': ((1,0),(0,-1)),
	'F': ((1,0),(0,1)),
	'.': (),
}
grid = []
for l in fileinput.input():
	grid.append([x for x in l.strip()])
seen = [[-1 for x in y] for y in grid]
for i in range(len(grid)):
	for j in range(len(grid[0])):
		if grid[i][j] == 'S':
			grid[i][j] = S
			seen[i][j] = 0
			#start = (i,j)
			a,b = tr[S][0]
			seen[i+a][j+b] = 1
			pos = (i+a, j+b)
dist = 1
while True:
	i,j = pos
	end = True
	dist += 1
	for a,b in tr[grid[i][j]]:
		#print(i,j,"->",i+a,j+b)
		if seen[i+a][j+b] < 0:
			end = False
			seen[i+a][j+b] = dist
			pos = (i+a,j+b)
	if end: break
print(dist//2)
