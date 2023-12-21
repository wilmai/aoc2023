import fileinput, heapq

conv = {
	('U','R'): (-0.5, -0.5), ('R','U'): (-0.5, -0.5),
	('D','R'): (0.5, -0.5), ('R','D'): (0.5, -0.5),
	('U','L'): (-0.5, 0.5), ('L','U'): (-0.5, 0.5),
	('D','L'): (0.5, 0.5), ('L','D'): (0.5, 0.5),
}
tr = {}

#input
prev = 'U'
x,y = 0,0
lines = []
for l in fileinput.input():
	d, n, c = l.strip().split()
	start = (x, y)
	c = c[2:-1]
	n, d = c[:-1], c[-1]
	n = int(n, 16)
	if d == '0': end = (x+n, y); d = 'R'
	elif d == '2': end = (x-n, y); d = 'L'
	elif d == '3': end = (x, y-n); d = 'U'
	else: end = (x, y+n); d = 'D'
	lines.append((start, end))
	shift = [sum(x) for x in zip(start, conv[(prev, d)])]
	tr[start] = shift
	print(start, end, n, shift, conv[(prev, d)])
	(x,y), prev = end, d
lines.append((end, lines[0][0]))

# trapezoid formula
tot = 0
for (x1,y1),(x2,y2) in lines:
	print(x1,y1,x2,y2)
	x1,y1 = tr[(x1,y1)]
	x2,y2 = tr[(x2,y2)]
	tot += (y1+y2)*(x1-x2)
print(tot/2)