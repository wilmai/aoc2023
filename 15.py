import fileinput

tot = 0
for l in fileinput.input():
	ss = l.strip().split(',')
	for s in ss:
		h = 0
		for c in s:
			h += ord(c)
			h = (h * 17) % 256
		print(s, h)
		tot += h
print(tot)