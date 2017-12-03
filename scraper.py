import json
import re

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

with open('stmt.txt') as f:
	lines = f.readlines()

	for line in lines: 
		if "Date" not in line:
			lines.remove(line)
		else:
			break

	lyfts = []
	ubers = []
	for line in lines: 
		if "LYFT" in line:
			lyfts.append(line)
		elif "UBER" in line:
			ubers.append(line)
	
	count = 0	
	for line in lyfts:
		count = count + 1
		print(line + str(count) + "\n")

	count = 0	
	for line in ubers:
		count = count + 1
		print(line + str(count) + "\n")

	rides = ubers + lyfts
	total = 0
	for line in rides:
		res = re.split("\s\s\s+|\n", line)
		for s in res:
			if is_number(s):
				num = float(s)
				if num < 0:
					total = total + num
		print line

	print total