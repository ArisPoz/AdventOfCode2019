def gravity(noun, verb):
	f = open("2_input.txt", "r")

	for line in f:
		list = line.rstrip().split(',')

	list[1] = noun
	list[2] = verb
	counter = 0
	for unit in list:

		if counter % 4 == 0 and counter !=0:
			var1 = int(list[counter-3]) 
			var2 = int(list[counter-2])
			set  = int(list[counter-1])
			if int(list[counter-4]) == 1:
				#print("position " + str(var1) + " and " + str(var2) + ": " + str(list[var1]) + " + " + str(list[var2]))
				sum = int(list[var1]) + int(list[var2])
				#print("Set to " + str(set) + " from " + str(list[set]) + " to " + str(sum))
				list[set] = sum
			elif int(list[counter-4]) == 2:
				#print("position " + str(var1) + " and " + str(var2) + ": " + str(list[int(var1)]) + " * " + str(list[var2]))
				mul = int(list[var1]) * int(list[var2])
				#print("Set to " + str(set) + " from " + str(list[set]) + " to " + str(mul))
				list[set] = mul
			elif int(list[counter-4]) == 99:
				#print("Code 99, break...")
				break
		counter = counter + 1
	return list[0]

for i in range(130):
	for j in range(130):
		if gravity(i,j) == 19690720:
			print(str(i)+str(j))
			break

