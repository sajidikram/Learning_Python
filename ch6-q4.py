myfile = open("infile", "r")
linefromfile = myfile.readline()
while linefromfile!='':
	print(linefromfile)
	linefromfile = myfile.readline()
myfile.close()