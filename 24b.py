import fileinput
import numpy as np
import random

hail = []
for l in fileinput.input():
	p, v = l.split('@')
	p, v = [int(x.strip()) for x in p.split(',')], [float(x.strip()) for x in v.split(',')]
	hail.append((np.array(p), np.array(v)))

# due to numerical stability problems lets try a few times
for i in range(10):
	random.shuffle(hail)
	left = []
	right = []
	x,y,z = 0,1,2
	for a,b in (hail[0:2], hail[2:4]):
		(Pa,Va),(Pb,Vb) = a,b
		# linear equations man..
		#Px,Py,Pz,Vz,Vy,Vz = C
		left.append([0, Vb[z]-Va[z], Va[y]-Vb[y], 0, Pa[z]-Pb[z], Pb[y]-Pa[y]])
		right.append([Va[y]*Pa[z] - Va[z]*Pa[y] + Vb[z]*Pb[y] - Vb[y]*Pb[z]])
		left.append([Va[z]-Vb[z], 0, Vb[x]-Va[x], Pb[z]-Pa[z], 0, Pa[x]-Pb[x]])
		right.append([Va[z]*Pa[x] - Va[x]*Pa[z] + Vb[x]*Pb[z] - Vb[z]*Pb[x]])
		left.append([Vb[y]-Va[y], Va[x]-Vb[x], 0, Pa[y]-Pb[y], Pb[x]-Pa[x], 0])
		right.append([Va[x]*Pa[y] - Va[y]*Pa[x] + Vb[y]*Pb[x] - Vb[x]*Pb[y]])
	res = np.linalg.solve(left, right)
	Pr = [int(round(v[0])) for v in res[:3]]
	print(sum(Pr), Pr)
