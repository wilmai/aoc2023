import fileinput, random
import numpy as np

def gaussian_elimination(left, right):
	mat = [l+r for l,r in zip(left, right)]
	h,k = 0,0
	while h < len(mat) and k < len(mat[0]):
		pivot = max((abs(mat[i][k]),i) for i in range(h, len(mat)))[1]
		if mat[pivot][k] == 0:
			k += 1
			continue
		mat[h], mat[pivot] = mat[pivot], mat[h]
		for i in range(h+1, len(mat)):
			f = mat[i][k]/mat[h][k]
			mat[i][k] = 0
			for j in range(k+1, len(mat[0])): mat[i][j] -= mat[h][j]*f
		h,k = h+1,k+1
	res = [1 for l in left[0]]
	for r in range(len(res)-1, -1, -1):
		m, acc = mat[r], mat[r][-1]
		for s in range(len(m)-2, r, -1): acc -= m[s]*res[s]
		res[r] = acc/m[r]
	return res

hail = []
for l in fileinput.input():
	p, v = l.split('@')
	p, v = [int(x.strip()) for x in p.split(',')], [int(x.strip()) for x in v.split(',')]
	hail.append((p, v))

x,y,z = 0,1,2
while True:
	random.shuffle(hail)
	left, right = [], []
	for a,b in (hail[0:2], hail[2:4]):
		(Pa,Va),(Pb,Vb) = a,b
		left.append([0, Vb[z]-Va[z], Va[y]-Vb[y], 0, Pa[z]-Pb[z], Pb[y]-Pa[y]])
		right.append([Va[y]*Pa[z] - Va[z]*Pa[y] + Vb[z]*Pb[y] - Vb[y]*Pb[z]])
		left.append([Va[z]-Vb[z], 0, Vb[x]-Va[x], Pb[z]-Pa[z], 0, Pa[x]-Pb[x]])
		right.append([Va[z]*Pa[x] - Va[x]*Pa[z] + Vb[x]*Pb[z] - Vb[z]*Pb[x]])
		left.append([Vb[y]-Va[y], Va[x]-Vb[x], 0, Pa[y]-Pb[y], Pb[x]-Pa[x], 0])
		right.append([Va[x]*Pa[y] - Va[y]*Pa[x] + Vb[y]*Pb[x] - Vb[x]*Pb[y]])
	res = gaussian_elimination(left, right)
	Pr = [int(round(v)) for v in res[:3]]
	Vr = [int(round(v)) for v in res[3:]]
	if all(np.dot(np.cross(Vr, Va), np.subtract(Pr, Pa)) == 0 for Pa,Va in hail):
		print(sum(Pr))
		break
