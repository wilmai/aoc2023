import fileinput

tot = 0
for l in fileinput.input():
	if not l.startswith("Game"): continue
	game, rest = l.split(":")
	gid = int(game.split()[1])
	games = rest.strip().split(";")
	mins = {"red": 0, "green": 0, "blue": 0}
	for game in games:
		cubes = game.split(",")
		for cube in cubes:
			num, col = cube.strip().split()
			num = int(num)
			mins[col] = max(mins[col], num)
	p = 1
	for k,v in mins.items():
		p *= v
	tot += p
	print(gid, p)
print(tot)
