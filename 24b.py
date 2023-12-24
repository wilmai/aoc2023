import fileinput, random
import numpy as np

hail = []
for l in fileinput.input():
	p, v = l.split('@')
	p, v = [int(x.strip()) for x in p.split(',')], [int(x.strip()) for x in v.split(',')]
	hail.append((p, v))

# due to numerical stability problems lets try a few times
x,y,z = 0,1,2
while True:
	random.shuffle(hail)
	left, right = [], []
	for a,b in (hail[0:2], hail[2:4]):
		(Pa,Va),(Pb,Vb) = a,b
		# Given rock = (Pr,Vr), two hailstones (Pa,Va) and (Pb,Vb)
		# (Pr - Pa) x (Vr - Va) - (Pr - Pb) x (Vr - Vb) = 0 vector
		# linear equation of 6 variables
		# Px,Py,Pz,Vx,Vy,Vz = C
		left.append([0, Vb[z]-Va[z], Va[y]-Vb[y], 0, Pa[z]-Pb[z], Pb[y]-Pa[y]])
		right.append([Va[y]*Pa[z] - Va[z]*Pa[y] + Vb[z]*Pb[y] - Vb[y]*Pb[z]])
		left.append([Va[z]-Vb[z], 0, Vb[x]-Va[x], Pb[z]-Pa[z], 0, Pa[x]-Pb[x]])
		right.append([Va[z]*Pa[x] - Va[x]*Pa[z] + Vb[x]*Pb[z] - Vb[z]*Pb[x]])
		left.append([Vb[y]-Va[y], Va[x]-Vb[x], 0, Pa[y]-Pb[y], Pb[x]-Pa[x], 0])
		right.append([Va[x]*Pa[y] - Va[y]*Pa[x] + Vb[y]*Pb[x] - Vb[x]*Pb[y]])
	res = np.linalg.solve(left, right)
	Pr = [int(round(v[0])) for v in res[:3]]
	Vr = [int(round(v[0])) for v in res[3:]]
	# validate with distance between two lines
	if all(np.dot(np.cross(Vr, Va), np.subtract(Pr, Pa)) == 0 for Pa,Va in hail):
		print(sum(Pr))
		break
