import fileinput, re
import bisect, sys

maps = []
for l in fileinput.input():
	l = l.strip()
	if len(l) == 0: continue
	if l.startswith("seeds:"):
		seeds = [int(x) for x in l.split(":")[1].split()]
	elif l.find(":") >= 0:
		maps.append([])
	else:
		dst, src, rng = [int(x) for x in l.strip().split()]
		maps[-1].append((src, dst, rng))

filled = []
for m in maps:
	m.sort()
	val = 0
	filled.append([])
	for src, dst, rng in m:
		if val < src:
			filled[-1].append((val, val, src - val))
		filled[-1].append((src, dst, rng))
		val = src+rng
	filled[-1].append((val, val, sys.maxsize - val))
# print(filled)

locs = []
for i in range(0, len(seeds), 2):
	vals = [seeds[i:i+2]]
	for m in filled:
		nxt = []
		for val, n in vals:
			while n > 0:
				#print("lookup", val, n, m)
				i = bisect.bisect(m, (val+1, 0, 0)) - 1
				src, dst, rng = m[i]
				rng = min(rng-(val-src), n)
				nxt.append((dst+val-src, rng))
				val += rng
				n -= rng
		#print(nxt)
		vals = nxt
	locs += vals

print(sorted(locs)[0][0])
