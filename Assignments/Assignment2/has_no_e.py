def has_no_e(value):
	
	for x in value:
		if value == 'e':
			return True
		else:
			return False



reader = open('gadsby_stripped.txt', 'r')
line = reader.readline()

while line:
	
	print(has_no_e(line))
