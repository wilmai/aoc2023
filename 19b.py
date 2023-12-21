import fileinput, re, math

rules = {}
vmap = {'x':0,'m':1,'a':2,'s':3}
for l in fileinput.input():
	l = l.strip()
	if len(l) == 0: break
	name, l = l[:-1].split('{')
	l = l.split(',')
	r, ru = [tuple(r.split(':')) for r in l[:-1]], []
	for c, d in r:
		if '>' in c:
			v, n = c.split('>')
			v, n = vmap[v], int(n)
			ru.append((v,n+1,5000,d))
		else:
			v, n = c.split('<')
			v, n = vmap[v], int(n)
			ru.append((v,0,n,d))
	ru.append((None, None, None, l[-1]))
	rules[name] = ru

def restrict(l1, h1, l2, h2): return (max(l1, l2), min(h1, h2))

cache = {}
def recurse(w, xmas):
	accept = math.prod(y-x for x,y in xmas)
	if accept == 0 or w == 'R': return 0
	if w == 'A': return accept
	key = (w, tuple(xmas))
	hit = cache.get(key)
	if hit is not None: return hit
	ways = 0
	for v,lo,hi,dest in rules[w]:
		if v is None:
			ways += recurse(dest, xmas)
			continue
		nxmas = xmas[:]; nxmas[v] = restrict(*xmas[v], lo, hi)
		ways += recurse(dest, nxmas)
		xmas[v] = restrict(*xmas[v], 0, lo) if lo > 0 else restrict(*xmas[v], hi, 5000)
	cache[key] = ways
	return ways

print(recurse('in', [(1,4001),(1,4001),(1,4001),(1,4001)]))