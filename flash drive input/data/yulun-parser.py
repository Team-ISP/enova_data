#import DecisionTree

input_file=open("training.csv","r")
output_file=open("output.txt","w")
array=[]
counter=0
for line in input_file:
	line=line.strip()
	split_string=line.split(";")

	counter=0
	while counter<len(split_string):
		if split_string[counter]=="\"NA\"":
			split_string[counter]=-1
		counter+=1


	home_ownership=split_string[1]
	del split_string [2]
	del split_string [2]
	del split_string [2]
	time=split_string[2]
	del split_string[3]
	del split_string[3]
	income_verif = split_string[3]
	if home_ownership== "\"RENT\"":
		split_string[1]=0
	elif home_ownership=="\"OWN\"":
		split_string[1]=1
	elif home_ownership=="\"MORTGAGE\"":
		split_string[1]=2
	elif home_ownership=="\"OTHER\"":
		split_string[1]=3
	elif home_ownership=="-1":
		split_string[1]=-1

	temp_arr=time.split(" ")
	#print "temp array is "
	#print temp_arr
	if len(temp_arr) > 1:
		split_string[2]=temp_arr[1]

	if income_verif== "\"Source Verified\"":
		split_string[3]=0
	elif income_verif== "\"Verified\"":
		split_string[3]=1
	elif income_verif== "\"Not Verified\"":
		split_string[3]=2

	#temp=split_string[23]
	#temp=temp[1:-2]

	temp=split_string[-8]
	if temp == "\"A\"":
		split_string[-8]=0
	if temp == "\"B\"":
		split_string[-8]=1
	if temp == "\"C\"":
		split_string[-8]=2
	if temp == "\"D\"":
		split_string[-8]=3
	if temp == "\"E\"":
		split_string[-8]=4
	if temp == "\"F\"":
		split_string[-8]=5
	if temp == "\"G\"":
		split_string[-8]=6


	temp=split_string[-7]
	if not temp==-1:
		split_string[-7]=temp[2:-1]





	temp=split_string[-6]
	if temp == "\"< 1 year\"":
		temp=0
	else:
		temp=temp[1:3]
	#temp=temp.strip()
	split_string[-6]=temp



	temp=split_string[-5]
	temp=temp[1:-2]
	split_string[-5]=temp


	temp=split_string[-2]

	if temp == "\"Fully Paid\"":
		split_string[-2]=0
	if temp == "\"Charged Off\"":
		split_string[-2]=1

	if split_string[-1]>0:
		split_string.append(1)
	else:
		split_string.append(0)

	array.append(split_string)

for elem in array:
	#print elem
	output_file.write(str(elem))
	output_file.write("\n")