import fileinput, re

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

def bounds_x(x):
	x = max(0, x)
	x = min(rx, x)
	return x
def bounds_y(y):
	y = max(0, y)
	y = min(ry, y)
	return y

for ny, x1, x2, num in nums:
	sym = False
	for y in range(bounds_y(ny-1), bounds_y(ny+2)):
		for x in range(bounds_x(x1-1), bounds_x(x2+1)):
			c = lines[y][x]
			if not c.isdigit() and c != '.':
				# print("symbol", y, x, c)
				sym = True
	if sym:
		tot += num

print(rx, ry)
# print(lines)
# print(nums)
print(tot)
