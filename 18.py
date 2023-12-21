import fileinput, heapq
#input
x,y,lx,ly,hx,hy = 0,0,0,0,0,0
lines = []
for l in fileinput.input():
	d, n, c = l.strip().split()
	n = int(n)
	start = (x, y)
	if d == 'R': end = (x+n, y)
	elif d == 'L': end = (x-n, y)
	elif d == 'U': end = (x, y-n)
	else: end = (x, y+n)
	lines.append((start, end, c))
	lx, ly, hx, hy = min(lx, x), min(ly, y), max(hx, x), max(hy, y)
	x,y = end
# build matrix
mat = [['.' for x in range(lx, hx+1)] for y in range(ly, hy+1)]
for (sx, sy), (ex, ey), c in lines:
	sx -= lx; sy -= ly; ex -= lx; ey -= ly
	dx = 1 if ex>=sx else -1; dy = 1 if ey>=sy else -1
	for x in range(sx, ex+dx, dx):
		for y in range(sy, ey+dy, dy):
			mat[y][x] = '#'

def fill(x, y, before, after):
	if mat[y][x] != before: return
	mat[y][x] = after
	cont = [(x,y)]
	while len(cont)>0:
		x,y = cont.pop()
		for nx,ny in ((x,y+1),(x,y-1),(x+1,y),(x-1,y)):
			if nx>=0 and ny>=0 and nx<len(mat[0]) and ny<len(mat):
				if mat[ny][nx] == before:
					mat[ny][nx] = after
					cont.append((nx,ny))
#borderfill
#for l in mat: print(''.join(l))
for y in range(len(mat)):
	fill(0, y, '.', 'O')
	fill(len(mat[0])-1, y, '.', 'O')
for x in range(len(mat[0])):
	fill(x, 0, '.', 'O')
	fill(x, len(mat)-1, '.', 'O')
#for l in mat: print(''.join(l))
print(sum(1 for y in range(len(mat)) for x in range(len(mat[0])) if mat[y][x] != 'O'))
