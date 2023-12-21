import fileinput
import math

times, dists = fileinput.input()
time = int(times.split(":")[1].strip().replace(" ", ""))
dist = int(dists.split(":")[1].strip().replace(" ", ""))
r1 = (-time - math.sqrt(time*time - 4 * dist)) / (-2)
r2 = (-time + math.sqrt(time*time - 4 * dist)) / (-2)
print(math.floor(r1) - math.ceil(r2) + 1)
