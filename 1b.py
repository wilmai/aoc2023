import fileinput, re

repl = [
	("one", 1),
	("two", 2),
	("three", 3),
	("four", 4),
	("five", 5),
	("six", 6),
	("seven", 7),
	("eight", 8),
	("nine", 9),
]

tot = 0
for l in fileinput.input():
	for word, num in repl:
		l = re.sub(word, word + str(num) + word, l)
	nums = [int(c) for c in l if c.isdigit()]
	if len(nums) > 0:
		num = nums[0] * 10 + nums[-1]
		print(num)
		tot += num
print(tot)
