import fileinput

cosmos = []
for l in fileinput.input():
	cosmos.append([0 if c == '.' else 1 for c in l.strip()])
space = [[1 for j in i] for i in cosmos]
expand = 1000000
for i in range(len(cosmos)):
	if sum(cosmos[i])==0:
		for j in range(len(cosmos[0])):
			space[i][j] = expand
for j in range(len(cosmos[0])):
	if sum([cosmos[i][j] for i in range(len(cosmos))])==0:
		for i in range(len(cosmos)):
			space[i][j] = expand
#for l in cosmos: print(l)
#for l in space: print(l)

galaxies = []
for i in range(len(cosmos)):
	for j in range(len(cosmos[0])):
		if cosmos[i][j] == 1:
			galaxies.append((i,j))
tot = 0
for a in range(len(galaxies)):
	for b in range(a+1, len(galaxies)):
		(i,j),(k,l) = galaxies[a], galaxies[b]
		vert = [space[x][j] for x in range(i, k, -1 if k < i else 1)]
		horz = [space[i][x] for x in range(j, l, -1 if l < j else 1)]
		tot += sum(vert) + sum(horz)
print(tot)