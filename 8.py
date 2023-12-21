import fileinput
import re

paths = {}
for line in fileinput.input():
	line = line.strip()
	if len(line) == 0: continue
	if line.count('=') == 0:
		pattern = line
	else:
		line = re.sub(r'[=,()]', '', line)
		node, left, right = line.split()
		paths[node] = (left, right)

step = 0
pos = 'AAA'
while pos != 'ZZZ':
	if pattern[step % len(pattern)] == 'L':
		pos = paths[pos][0]
	else:
		pos = paths[pos][1]
	step += 1
print(step)
