import fileinput

mat = []
for l in fileinput.input():
	l = l.strip()
	mat.append([c for c in l])
tot = 0
print(len(mat), len(mat[0]))
for yt in range(len(mat)):
	for x in range(len(mat[0])):
		y = yt
		if mat[y][x] == 'O':
			print(y, x)
			mat[y][x] = '.'
			while y > 0 and mat[y][x] == '.': y -= 1
			if mat[y][x] != '.': y += 1
			mat[y][x] = 'O'
			tot += len(mat) - y
for l in mat: print(''.join(l))
print(tot)
