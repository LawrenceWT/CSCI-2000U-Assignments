def has_no_e(value):
	
	if value == 'e':
		return True
	else:
		return False



reader = open('gadsby_stripped.txt', 'r')
line = reader.readline()

print(has_no_e(line))
