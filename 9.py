import fileinput
import re

tot = 0
for l in fileinput.input():
	v = [[int(x) for x in l.strip().split()]]
	while not all([x==0 for x in v[-1]]):
		v.append([b-a for a, b in zip(v[-1], v[-1][1:])])
	print(v)
	v.reverse()
	add = 0
	for d in v[1:]:
		add = d[-1] + add
	print(add)
	tot += add
print(tot)
