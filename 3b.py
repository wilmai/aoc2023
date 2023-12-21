import fileinput, re, math

tot = 0
rx = ry = 0

lines = []
nums = []

for l in fileinput.input():
	l = l.strip()
	if len(l) == 0: continue
	if rx == 0: rx = len(l)
	# grab nums
	for m in re.finditer(r'[0-9]+', l):
		nums.append((ry, m.start(), m.end(), int(m.group())))
	ry += 1
	lines.append(l)

def bounds(x, mx):
	x = max(0, x)
	x = min(mx, x)
	return x

gears = {}

for ny, x1, x2, num in nums:
	sym = False
	for y in range(bounds(ny-1,ry), bounds(ny+2,ry)):
		for x in range(bounds(x1-1,rx), bounds(x2+1,rx)):
			c = lines[y][x]
			if c == '*':
				# print("gear", y, x)
				gears[(y,x)] = gears.get((y,x), []) + [(ny, x1, num)]

for gearlist in gears.values():
	if len(gearlist) == 2:
		mul = math.prod([n for y,x,n in gearlist])
		print("gear", gearlist, mul)
		tot += mul

print(rx, ry)
# print(lines)
# print(nums)
print(tot)
