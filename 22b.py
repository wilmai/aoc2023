import fileinput

blocks = []
for l in fileinput.input():
	a,b = [tuple(int(x) for x in y.split(',')) for y in l.strip().split('~')]
	blocks.append((a,b))
blocks = sorted(blocks, key=lambda b: tuple(reversed(b[0])))

def each_cube(a,b):
	for t in ((x,y,z) for x in range(a[0],b[0]+1) for y in range(a[1],b[1]+1) for z in range(a[2],b[2]+1)):
		yield t

support = {}
mat = {}
for i,(a,b) in enumerate(blocks):
	height = a[2]
	fall, colliders = 0, []
	for fall in range(1, height):
		for x,y,z in each_cube(a,b):
			z -= fall
			coll = mat.get((x,y,z))
			if coll is not None: colliders.append(coll)
		if len(colliders)>0:
			fall -= 1 # backup one level
			colliders = tuple(sorted(set(colliders)))
			support[colliders] = support.get(colliders, set()).union((i,))
			break
	for x,y,z in each_cube(a,b):
		z -= fall
		mat[(x,y,z)] = i

tot = 0
for i in reversed(range(len(blocks))):
	fall, count = set((i,)), 0
	while len(fall) > count:
		for k,v in support.items():
			if set(k).issubset(fall):
				fall = fall.union(v)
		count = len(fall)
	tot += count - 1
	#print("disintegrating", i, "fells", len(fall)-1)
print(tot)
