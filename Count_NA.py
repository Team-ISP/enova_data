#count how many NAs there is
f = open ("training.csv", "r")
NA_counter = 0
no_NA_line = 0
for line in f:
	line=line.strip()
	split_string=line.split(";")
	for word in split_string:
		if word == "NA":
			NA_counter++
			continue
		no_NA_line++
