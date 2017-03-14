#Create a small dataset to test the different parameters of SVM. 
#I want to have a dataset that is equally distributed as my 70aadata set, which is 38% of the proteins have a signal peptide. 
#I will take 100 proteins, so 38 prots with Signal Peptide and 62 proteins without

from sklearn.utils import shuffle
import sys

f = open("//home/u2195/Desktop/Dropbox/Bioinformatics_projects/data/70aadata.txt","r")
datalist = list()
for line in f:
	newline = line.strip()
	datalist.append (newline)
titlelist = list ()
seqlist = list()
structurelist = list()
for i in datalist [:: 3]:
	titlelist.append (i)
for i in datalist[1::3]:
	seqlist.append (i)
for i in datalist[2::3]:
	structurelist.append (i)

#sklearns randomizer funtion called shuffle

y = list(zip(titlelist, seqlist, structurelist))
randomized = shuffle(y)
titlelist=[randomized [i][0] for i in range (0, len(randomized))]
seqlist=[randomized [i][1] for i in range (0, len(randomized))]
structurelist=[randomized [i][2] for i in range (0, len(randomized))]

shit=[]
crap=[]

for i in range(0, len(randomized)):
	theset = set([i for i in randomized [i][2]])
	if 'S' not in theset:
		shit.append(randomized[i])
	if len(shit)==310:
		break
#print(shit)
#print(len(shit))

for i in range(0, len(randomized)):
	theset = set([i for i in randomized [i][2]])	
	if ('S' in theset) and ('G' in theset):
		crap.append(randomized[i])
	if len(crap)==190:
		break
#print(crap)
#print(len(crap))
poo=shit+crap
print(poo)
print(len(poo))

with open ('//home/u2195/Desktop/Dropbox/Bioinformatics_projects/data/500seqdata.txt', 'w')as b:
	for i in range(0, len(poo)):
		b.write(poo [i][0]+'\n')
		b.write(poo [i][1]+'\n')
		b.write(poo [i][2]+'\n')


		
	
