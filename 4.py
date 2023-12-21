import fileinput, re

tot = 0

for l in fileinput.input():
	l = l.strip()
	if len(l) == 0: continue
	card, l = l.split(":")
	wins, nums = l.split("|")
	wins = [int(x) for x in wins.strip().split()]
	nums = [int(x) for x in nums.strip().split()]
	res = [(x in wins) for x in nums]
	score = (1 << sum([1 for x in nums if x in wins])) >> 1
	tot += score
	print(card, res, score)
print(tot)