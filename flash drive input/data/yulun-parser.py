input_file=open("training.csv","r")
array=[]
for line in input_file:
	line=line.strip()
	split_string=line.split(";")
	array.append(split_string)
x=array[0]
y=array[1]

cap=len(array[0])
counter=0
while (counter<cap):
	print x[counter]
	print y[counter]
	counter+=1