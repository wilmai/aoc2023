import fileinput, re

rules = {}
parts = []
rate = False
for l in fileinput.input():
	l = l.strip()
	if len(l) == 0: rate = True; continue
	if not rate:
		name, l = l[:-1].split('{')
		l = l.split(',')
		rules[name] = [tuple(r.split(':')) for r in l[:-1]] + [(None, l[-1])]
		print(name, rules[name])
	else:
		parts.append([int(x) for x in re.findall(r'[0-9]+', l)])
		print(parts[-1])

tot = 0
for x,m,a,s in parts:
	work = 'in'
	while True:
		for cond, res in rules[work]:
			if cond is None or eval(cond):
				work = res
				break
		if work == 'R' or work == 'A':
			if work == 'A':
				tot += sum((x,m,a,s))
			break
print(tot)