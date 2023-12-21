import fileinput

def permute(n, t):
	if n == 1:
		yield [t]
	elif t >= 0:
		take = 1 if n > 2 else 0
		top = t - (n-3 if n > 2 else 0)
		for i in range(take, top+1):
			for p in permute(n-1, t-i):
				yield [i] + p
	else:
		yield []

def render(l, c):
	dots = ['.'*x for x in [l[-2]]+l[:-2]+[l[-1]]]
	checks = ['#'*x for x in c]
	tot = dots + checks
	tot[::2] = dots
	tot[1::2] = checks
	s = ''.join(tot)
	#print(s)
	return s

tot = 0
for l in fileinput.input():
	state, check = l.strip().split()
	state = state.strip('.')
	check = [int(x) for x in check.split(',')]
	chars = len(state) - sum(check)
	# print(state, len(state) - sum(check))
	checks = len(check)+1
	sol = 0
	for p in permute(checks, chars):
		p = render(p, check)
		if all(p[i] == state[i] or state[i] == '?' for i in range(len(state))):
			sol += 1
	print(sol)
	tot += sol
print(tot)