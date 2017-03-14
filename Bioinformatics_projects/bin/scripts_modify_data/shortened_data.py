f= open ('/home/u2195/Desktop/Dropbox/Bioinformatics_projects/data/globular_signal_peptide_2state.txt', 'r')
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
	seqlist.append(i[0:70])
for i in datalist[2::3]:
	structurelist.append(i[0:70])

with open ('//home/u2195/Desktop/Dropbox/Bioinformatics_projects/data'+ '/' + '70aadata' '.txt', 'w')as b:
	for i in range(len(titlelist)):
		b.write(titlelist[i]+'\n')
		b.write(seqlist[i]+'\n')
		b.write(structurelist[i]+'\n')
		b.close


