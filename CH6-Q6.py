myfile = open("data.txt", "r")
count=0
sum=0
linefromfile = myfile.readline()
while linefromfile!='':
	print(linefromfile)
	sum=sum+int(linefromfile)
	count=count+1
	linefromfile = myfile.readline()
myfile.close()
avg=sum/count
print("The sum of",count,"numbers is", sum)
print("Average =",avg)