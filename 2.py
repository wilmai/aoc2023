import fileinput

tot = 0
for l in fileinput.input():
	if not l.startswith("Game"): continue
	game, rest = l.split(":")
	gid = int(game.split()[1])
	games = rest.strip().split(";")
	poss = True
	for game in games:
		cubes = game.split(",")
		for cube in cubes:
			num, col = cube.strip().split()
			num = int(num)
			if col == "red" and num > 12: poss = False
			if col == "green" and num > 13: poss = False
			if col == "blue" and num > 14: poss = False
	if poss:
		tot += gid
		print("possible")
	else:
		print("impossible")
	print(gid)
print(tot)
