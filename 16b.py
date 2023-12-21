import fileinput

mat = []
for l in fileinput.input(): mat.append(l.strip())
dmap = {
	(0,'.'): [(0,0,1)], #right
	(1,'.'): [(1,1,0)], #down
	(2,'.'): [(2,0,-1)], #left
	(3,'.'): [(3,-1,0)], #up
	(0,'|'): [(1,1,0),(3,-1,0)], #split up/down
	(1,'|'): [(1,1,0)], #down
	(2,'|'): [(1,1,0),(3,-1,0)], #split up/down
	(3,'|'): [(3,-1,0)], #up
	(0,'-'): [(0,0,1)], #right
	(1,'-'): [(0,0,1),(2,0,-1)], #split left/right
	(2,'-'): [(2,0,-1)], #left
	(3,'-'): [(0,0,1),(2,0,-1)], #split left/right
	(0,'/'): [(3,-1,0)], #up
	(1,'/'): [(2,0,-1)], #left
	(2,'/'): [(1,1,0)], #down
	(3,'/'): [(0,0,1)], #right
	(0,'\\'): [(1,1,0)], #down
	(1,'\\'): [(0,0,1)], #right
	(2,'\\'): [(3,-1,0)], #up
	(3,'\\'): [(2,0,-1)], #left
}

def energ(start):
	buf = [start]
	state = [[[0 for x in y] for y in mat] for d in range(4)]
	while len(buf)>0:
		d,y,x = buf.pop()
		if y < 0 or y >= len(mat) or x < 0 or x >= len(mat[0]): continue
		if state[d][y][x]: continue
		state[d][y][x] = 1
		for dd,dy,dx in dmap[(d, mat[y][x])]:
			buf.append((dd, y+dy, x+dx))
	energ = [1 if any(state[d][y][x] for d in range(4)) else 0 for x in range(len(mat[0])) for y in range(len(mat))]
	return sum(energ)

best = 0
best = max([energ((0,y,0)) for y in range(len(mat))]+[best])
best = max([energ((2,y,len(mat[0])-1)) for y in range(len(mat))]+[best])
best = max([energ((1,0,x)) for x in range(len(mat[0]))]+[best])
best = max([energ((3,len(mat)-1,x)) for x in range(len(mat[0]))]+[best])
print(best)
