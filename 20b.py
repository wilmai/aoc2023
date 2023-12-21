import fileinput, re, math
from collections import deque

conn = {}
for l in fileinput.input():
	m = re.match(r'([%&]?)([a-z]+) -> (.*)', l.strip())
	typ, name, out = m.groups()
	out = [x.strip() for x in out.split(',')]
	conn[name] = (typ, out)
	#if 'cs' in out: print(name, typ, out)
conn['rx'] = ('O', [])
conn['output'] = ('O', [])
idx = {name:i for i,name in enumerate(conn.keys())}
ridx = {i:name for i,name in enumerate(conn.keys())}
state = [False]*len(idx)
wire = [[None for y in range(len(idx))] for x in range(len(idx))]
ntype = [typ for x,(typ,out) in conn.items()]
out = [[idx[v] for v in o] for x,(t,o) in conn.items()]
#print('idx', idx, state, wire, ntype, out)
bcnode = idx['broadcaster']
bcast = out[bcnode]
print(bcast)
for v,o in enumerate(out):
	for w in o:
		wire[w][v] = False

oid = [idx[x] for x in ['kh', 'lz', 'tg', 'hn']]
cycles = []
print(oid)
for i in range(10000):
	dq = deque([(bcnode, n, False) for n in bcast])
	while len(dq)>0:
		src,dst,val = dq.popleft()
		if dst in oid and not val:
			print('output', dst, i)
			cycles.append(i+1)
		wire[dst][src] = val
		if not val: state[dst] = not state[dst]
		for n in out[dst]:
			if ntype[dst] == '%':
				if not val: dq.append((dst, n, state[dst]))
			elif ntype[dst] == '&':
				dq.append((dst, n, not all(x for x in wire[dst] if x is not None)))
			else: assert(False)

print(math.lcm(*cycles[:4]))
