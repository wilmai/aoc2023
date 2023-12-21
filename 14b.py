import fileinput

mat = []
for l in fileinput.input():
	l = l.strip()
	mat.append([c for c in l])

def cycle(mat):
	for i in range(4):
		for yt in range(len(mat)):
			for x in range(len(mat[0])):
				y = yt
				if mat[y][x] == 'O':
					mat[y][x] = '.'
					while y > 0 and mat[y][x] == '.': y -= 1
					if mat[y][x] != '.': y += 1
					mat[y][x] = 'O'
		mat = [list(x) for x in zip(*mat[::-1])]
		tot = sum([len(mat)-y for y in range(len(mat)) for x in range(len(mat[0])) if mat[y][x]=='O'])
	return mat, tot

cycles = 1000
cache, cc, tc = {}, {}, {}
for i in range(1, cycles+1):
	tmat = tuple(tuple(y) for y in mat)
	nmat = cache.get(tmat)
	if nmat is None:
		mat, tot = cycle(mat)
		cache[tmat] = mat
		tc[i] = tot
		cc[tmat] = i
	else:
		lam, mu = cc[tmat], i-cc[tmat]
		print("CYCLE", i, cc[tmat])
		break

c = lam + (1000000000 - lam) % mu
print("ANS:", c, tc[c])
