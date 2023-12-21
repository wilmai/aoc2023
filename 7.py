import fileinput
import copy

cards = "23456789TJQKA"

hands = []
for line in fileinput.input():
	line = line.strip()
	if len(line) == 0: continue
	hand, bid = line.strip().split()
	score = sorted([hand.count(c) for c in cards], reverse=True)
	rep = [cards.find(c) for c in hand]
	hands.append([hand, rep, int(bid), score])

def sort_fn(details):
	hand, rep, bid, score = details
	return (score, rep)
hands.sort(key=sort_fn)

tot = 0
for i in range(len(hands)):
	hand, rep, bid, score = hands[i]
	tot += bid * (i+1)
print(tot)
