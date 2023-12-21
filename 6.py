import fileinput, re
import bisect, sys

times, dists = fileinput.input()
times = [int(x) for x in times.split(":")[1].strip().split()]
dists = [int(x) for x in dists.split(":")[1].strip().split()]

tot = 1
for race in range(len(times)):
	time = times[race]
	dist = dists[race]
	wins = 0
	for t in range(time):
		sim = (time - t) * t
		if sim > dist: wins += 1
		#print(time, dist, t, sim)
	tot *= wins

print(tot)
