filename=input("Enter filename : ")
myfile=open(filename,"w")
for i in range(1,11):
	myfile.write(str(i)+'\n')
myfile.close()