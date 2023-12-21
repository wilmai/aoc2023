import fileinput, heapq

mat = []
for l in fileinput.input(): mat.append([int(x) for x in l.strip()])

state = [[[1000000000 for x in y] for y in mat] for d in range(2)]
buf = [(0,0,0,0), (0,1,0,0)]
heapq.heapify(buf)

def cart(dist, dr, ax, ay, bx, by):
	dx = 1 if bx>ax else -1
	dy = 1 if by>ay else -1
	for y in range(ay+dy, by+dy, dy):
		for x in range(ax+dx, bx+dx, dx):
			if y < 0 or y >= len(mat): continue
			if x < 0 or x >= len(mat[0]): continue
			dist += mat[y][x]
			#print('push', dist, dr, x, y)
			heapq.heappush(buf, (dist, dr, x, y))

while len(buf)>0:
	c,d,x,y = heapq.heappop(buf)
	if c >= state[d][y][x]: continue
	state[d][y][x] = c
	#print(c,d,x,y)
	if d == 0:
		cart(c, 1, x-1, y, x, y+3)
		cart(c, 1, x-1, y, x, y-3)
	else:
		cart(c, 0, x, y-1, x+3, y)
		cart(c, 0, x, y-1, x-3, y)

print(min(state[0][len(mat)-1][len(mat[0])-1], state[1][len(mat)-1][len(mat[0])-1]))
