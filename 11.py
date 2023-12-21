import fileinput

cosmos = []
for l in fileinput.input():
	cosmos.append([0 if c == '.' else 1 for c in l.strip()])
#for l in cosmos: print(l)

for expansion in range(2):
	nxt = []
	for l in cosmos:
		nxt.append(l)
		if sum(l)==0: nxt.append(l)
	nxt = [[nxt[i][j] for i in range(len(nxt))] for j in range(len(nxt[0]))]
	cosmos = nxt
	#for l in cosmos: print(l)

galaxies = []
for i in range(len(cosmos)):
	for j in range(len(cosmos[0])):
		if cosmos[i][j] == 1:
			galaxies.append((i,j))
tot = 0
for i,j in galaxies:
	for k,l in galaxies:
		tot += abs(i-k)+abs(j-l)
print(tot//2)