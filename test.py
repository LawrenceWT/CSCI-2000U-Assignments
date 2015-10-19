num = 0
while num <=10:
	if (num % 2) == 1:
		print(num)
	num += 1


loop = 0
while loop <= 10:
	print('')
	loop += 1



num2 = 2

while num2 <= 10:
	is_prime = True 
	trial = 2
	while trial < num2:
		if (num2 % trial) == 0:
			is_prime = False
		trial += 1 
	if is_prime:
			print(num2)
	num2 +=1