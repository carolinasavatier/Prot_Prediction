#Analyze the proportion of features I have in my data (G and S)
f = open("../data/70aadata.txt","r")
datalist = list()
structurelist=list()
for line in f:
	newline = line.replace ("\n", "")
	datalist.append (newline)
for i in datalist[2::3]:
	structurelist.append (i)

Gcount=0
for i in range (len (structurelist)):
	for j in range (0, len(structurelist[i])):
		if structurelist[i][j] ==  'G':
			Gcount = Gcount +1
print ("G count is ", Gcount)

Scount=0
for i in range (len (structurelist)):
	for j in range (0, len(structurelist[i])):
		if structurelist[i][j] ==  'S':
			Scount = Scount +1
print ("S count is ", Scount)

S_percentage = ((int(Scount)/int(Gcount))*100)
print ("Percentage of S is %r ." %S_percentage)

with open ('//home/u2195/Desktop/Dropbox/Bioinformatics_projects/results'+ '/' + 'Feature_percent' + '.txt', 'w')as b:
	b.write("G count is "+ str(Gcount)+'\n')
	b.write("S count is "+ str(Scount)+'\n')
	b.write("Percentage of S is %r ." + str(S_percentage))
	b.close
