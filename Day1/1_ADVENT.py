import math

def rec(fuel):
	if fuel <= 0:
		return 0
	else:
		return fuel + rec(math.floor(fuel / 3) - 2)
	
f = open("1_input.txt", "r")
lines = f.readlines()
total = 0
extra = 0
for line in lines:
	calc = math.floor(int(line) / 3) - 2
	calc_e = rec(calc)
	total += calc
	extra += calc_e

print("total: " + str(total))
print("extra: " + str(extra))

#3269236

