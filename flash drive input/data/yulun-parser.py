input_file=open("training.csv","r")
array=[]
for line in input_file:
	line=line.strip()
	split_string=line.split(";")
	array.append(split_string)
print array[0]
print array[1]