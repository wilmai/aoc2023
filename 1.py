import fileinput

tot = 0
for l in fileinput.input():
	nums = [int(c) for c in l if c.isdigit()]
	if len(nums) > 0:
		tot += nums[0] * 10 + nums[-1]
print(tot)
