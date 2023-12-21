import fileinput
import copy

cards = "J23456789TQKA"

hands = []
for line in fileinput.input():
	line = line.strip()
	if len(line) == 0: continue
	hand, bid = line.strip().split()
	scores = []
	for c in cards:
		joker = hand.replace('J', c)
		scores.append(sorted([joker.count(c) for c in cards], reverse=True))
	scores.sort()
	rep = [cards.find(c) for c in hand]
	hands.append([hand, rep, int(bid), scores[-1]])

def sort_fn(details):
	hand, rep, bid, score = details
	return (score, rep)
hands.sort(key=sort_fn)

tot = 0
for i in range(len(hands)):
	hand, rep, bid, score = hands[i]
	tot += bid * (i+1)
print(tot)
