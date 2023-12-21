import fileinput

state = []
cache = {}

def permute(idx, check):
	look = cache.get((idx, tuple(check)))
	if look is not None: return look
	if len(check) == 0:
		return 1 if all(state[i] != '#' for i in range(idx, len(state))) else 0
	if idx >= len(state): return 0
	if idx+max(sum(check)+len(check)-1, 0) > len(state): return 0
	while state[idx] == '.': idx += 1
	ch = check[0]
	# try #s
	ways = 0
	if idx+ch <= len(state) and all(state[i] != '.' for i in range(idx, idx+ch)):
		if idx+ch == len(state) or state[idx+ch] != '#':
			nxt = idx+ch if idx+ch == len(state) else idx+ch+1
			#print(state[idx:nxt], state[nxt:], ch, check[1:])
			ways += permute(nxt, check[1:])
	# try dot
	if state[idx] == '?':
		ways += permute(idx+1, check)
	cache[(idx, tuple(check))] = ways
	return ways

tot = 0
for l in fileinput.input():
	state, check = l.strip().split()
	state = '?'.join([state for i in range(5)]).strip('.')
	check = [int(x) for x in check.split(',')]*5
	cache = {}
	p = permute(0, check)
	print(p)
	tot += p
print(tot)
