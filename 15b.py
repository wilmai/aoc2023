import fileinput

box = [[] for x in range(256)]

def hash(s):
	h = 0
	for c in s:
		h += ord(c)
		h = (h * 17) % 256
	return h

tot = 0
for l in fileinput.input():
	ss = l.strip().split(',')
	for s in ss:
		if '-' in s:
			print('-')
			label = s.split('-')[0]
			h = hash(label)
			print(s, h, box[h], [x for x in box[h] if x[0] != label])
			box[h] = [x for x in box[h] if x[0] != label]
		else:
			print('=')
			label,lens  = s.split('=')
			h = hash(label)
			lens = int(lens)
			print(s, h, box[h])
			box[h] = [(l,lens) if label == l else (l,m) for l,m in box[h]]
			if not any(l == label for l,m in box[h]):
				box[h].append((label, lens))
			print(s, h, box[h])
print(box)

tot = 0
for h in range(len(box)):
	b = box[h]
	for s in range(len(b)):
		tot += b[s][1] * (s+1) * (h+1)
print(tot)