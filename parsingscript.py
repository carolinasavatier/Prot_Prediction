#Create one big list with the whole raw data file (each line is an element of the list, so we have title1, sequence1, structure1, title2...). Then create a list with all the titles,titlelist, another with all the sequences, seqlist, and another with all the structures, structurelist)

#import pandas as pd
f = open ('/home/u2195/Desktop/Bioinformatics_projects/data/text.txt', 'r')
datalist = list()
for line in f:
	newline = line.replace ("\n", "")
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

#Define the window size

window = 3

#To be able to access each amino acid, we need to take each sequence of seqlist and make a list of it, where each element is an aminoacid 

aalist= list()
for seq in seqlist:
	list(seq)
	aalist.extend (list(seq))
print(seqlist)
print (len(seqlist))
print(aalist[:10])
print(len(aalist))

#Create the window






