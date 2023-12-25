import fileinput
import networkx
import numpy as np

nodes = set()
G = networkx.DiGraph()
for l in fileinput.input():
	n, links = l.split(':')
	links = links.strip().split()
	for l in links:
		G.add_edge(n, l, capacity=1)
		G.add_edge(l, n, capacity=1)
		nodes.add(n), nodes.add(l)

for m in nodes:
	for n in nodes:
		if m >= n: continue
		cut, partition = networkx.minimum_cut(G, m, n)
		if cut == 3:
			print(np.multiply(*[len(p) for p in partition]))
			exit(0)
