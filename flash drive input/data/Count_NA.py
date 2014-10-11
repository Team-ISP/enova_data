#count how many NAs there is
f = open ("training.csv", "r")
counter = 0
for line in f:
	line=line.strip()
	split_string=line.split(";")
	for word in split_string:
		if word == "NA":
			counter++
return counter


