import fileinput, re

mat = []
for l in fileinput.input():
	l = re.sub(r'[<>v^]', '.', l)
	mat.append([x for x in l.strip()])
for x in range(len(mat[0])):
	if mat[0][x]=='.': start = (x,0)
	if mat[len(mat)-1][x]=='.': end = (x,len(mat)-1)
verts = [(x,y) for y in range(len(mat)) for x in range(len(mat[0])) if mat[y][x] != '#']
edges = {}
for x,y in verts:
	tile, outs = mat[y][x], []
	for d,nx,ny in (('>',x+1,y),('<',x-1,y),('^',x,y-1),('v',x,y+1)):
		if nx>=0 and ny>=0 and nx<len(mat[0]) and ny<len(mat) and mat[ny][nx] != '#':
			if tile == '.' or tile == d:
				outs.append((nx,ny))
	edges[(x,y)] = outs
# points of interest: cells with >2 adjacencies, start & end
interest, links = [v for v,e in edges.items() if len(e) > 2] + [start, end], {}
for iv in interest:
	outs = []
	for ov in edges[iv]:
		pv, nv, steps = iv, ov, 1
		while nv not in interest:
			t = nv
			nv, = [x for x in edges[nv] if x != pv]
			pv = t
			steps += 1
		outs.append((nv, steps))
	links[iv] = outs
print("links", links) # dfs longest path through links
stack, vis, best = [(start, 0)], set(), 0
while len(stack)>0:
	p, tot = stack[-1]
	if p in vis:
		vis.remove(stack.pop()[0])
		continue
	vis.add(p)
	if p == end and tot > best:
		best = tot
		print(best)
	for q, steps in links[p]:
		if q not in vis:
			stack.append((q, tot+steps))
