import fileinput

hail = []
for l in fileinput.input():
	p, v = l.split('@')
	p, v = [int(x.strip()) for x in p.split(',')], [int(x.strip()) for x in v.split(',')]
	hail.append((tuple(p), tuple(v)))
print(hail)

#bounds = (7, 27)
bounds = (200000000000000, 400000000000000)
count = 0
for i1,h1 in enumerate(hail):
	for i2,h2 in enumerate(hail):
		if i1 >= i2: continue
		(p1,v1),(p2,v2) = h1,h2
		d = v2[0]*v1[1]-v2[1]*v1[0]
		if d == 0: continue
		diff = (p2[0]-p1[0], p2[1]-p1[1])
		u = (diff[1]*v2[0] - diff[0]*v2[1])/d
		v = (diff[1]*v1[0] - diff[0]*v1[1])/d
		if u < 0 or v < 0: continue
		hit = (p1[0]+u*v1[0], p1[1]+u*v1[1])
		if all(x>=bounds[0] and x<=bounds[1] for x in hit):
			print(h1, h2, hit)
			count += 1
print(count)
