import fileinput

blocks = []
for l in fileinput.input():
	a,b = l.strip().split('~')
	a,b = [tuple(int(x) for x in y.split(',')) for y in (a,b)]
	blocks.append((a,b))
blocks = sorted(blocks, key=lambda b: tuple(reversed(b[0])))

def each_cube(a,b):
	for t in ((x,y,z) for x in range(a[0],b[0]+1) for y in range(a[1],b[1]+1) for z in range(a[2],b[2]+1)):
		yield t

#supporting = [[] for x in blocks]
resting = {}
mat = {}
for i,(a,b) in enumerate(blocks):
	#print(i, (a,b))
	resting[i] = []
	height = a[2]
	fall = 0
	colliders = []
	for fall in range(1, height):
		for x,y,z in each_cube(a,b):
			z -= fall
			coll = mat.get((x,y,z))
			if coll is not None: colliders.append(coll)
		if len(colliders)>0:
			fall -= 1 # backup one level
			resting[i] = tuple(set(colliders))
			break
	#print(i, "fell", fall, "resting on", resting[i], "height", height-fall)
	for x,y,z in each_cube(a,b):
		z -= fall
		mat[(x,y,z)] = i
print(len(blocks) - len(set(v[0] for k,v in resting.items() if len(v)==1)))