import fileinput
import re
import math

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

starts = [p for p in paths.keys() if p.endswith('A')]
cycles = []
for pos in starts:
	step = 0
	while not pos.endswith('Z'):
		branch = 0 if pattern[step % len(pattern)] == 'L' else 1
		pos = paths[pos][branch]
		step += 1
	cycles.append(step)
print(cycles)
print(math.lcm(*cycles))
