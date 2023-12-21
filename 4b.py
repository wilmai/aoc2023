import fileinput, re

tot = 0

cards = []

for l in fileinput.input():
	l = l.strip()
	if len(l) == 0: continue
	card, l = l.split(":")
	wins, nums = l.split("|")
	wins = [int(x) for x in wins.strip().split()]
	nums = [int(x) for x in nums.strip().split()]
	score = sum([1 for x in nums if x in wins])
	cards.append(score)
	print(card, score)

wins = [0 for x in cards]

for i in range(len(cards)-1, -1, -1):
	score = cards[i]
	# tot += 1
	extras = 1
	for j in range(i+1, i+1+score):
		#print(i, j, wins[j])
		extras += wins[j]
	wins[i] = extras
	tot += extras
	#print("score:", i, extras, tot)
print(tot)
