import fileinput

mat = []
for l in fileinput.input():
	mat.append([x for x in l.strip()])
for x,v in enumerate(mat[0]):
	if v == '.': start = (x,0)
for x,v in enumerate(mat[-1]):
	if v == '.': end = (x,len(mat)-1)
print(start, end)
verts = [(x,y) for y in range(len(mat)) for x in range(len(mat[0])) if mat[y][x] != '#']
dist = {(x,y):1000000 for x,y in verts}
dist[start] = 0
prev = {(x,y):None for x,y in verts}
print("verts", len(verts))
edges = {}
for x,y in verts:
	tile = mat[y][x]
	outs = []
	for d,nx,ny in (('>',x+1,y),('<',x-1,y),('^',x,y-1),('v',x,y+1)):
		if nx>=0 and ny>=0 and nx<len(mat[0]) and ny<len(mat) and mat[ny][nx] != '#':
			if tile == '.' or tile == d:
				outs.append((nx,ny))
	edges[(x,y)] = outs

best, bpath = 0, []
vis = set()
stack = [(start,0)]
while len(stack)>0:
	v,steps = stack[-1]
	if v in vis:
		vis.remove(v)
		stack.pop()
		continue
	vis.add(v)
	if v == end and steps > best:
		print("best", best, steps)
		best = steps
		#bpath = sorted(list(vis))
	for nv in edges[v]:
		if not nv in vis:
			stack.append((nv, steps+1))
