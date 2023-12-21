import fileinput, re
import bisect

tot = 0
maps = []

for l in fileinput.input():
	l = l.strip()
	if len(l) == 0: continue

	if l.startswith("seeds:"):
		seeds = [int(x) for x in l.split(":")[1].split()]
		continue
	if l.find(":") >= 0:
		maps.append([])
		continue
	dst, src, rng = [int(x) for x in l.strip().split()]
	maps[-1].append((src, dst, rng))

for m in maps:
	m.sort()

locs = []

for val in seeds:
	print(val)
	for m in maps:
		i = bisect.bisect(m, (val+1, 0, 0)) - 1
		if i < 0 or i >= len(m):
			print(val, m, val)
			continue
		src, dst, rng = m[i]
		assert val >= src
		if val >= src+rng:
			print(val, m, val)
			continue
		print(val, m, i, dst+val-src)
		val = dst+val-src
	locs.append(val)

print(sorted(locs)[0])
