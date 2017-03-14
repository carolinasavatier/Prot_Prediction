#File to parse my database and put each title+sequence into fasta format and store it in individual files
f = open("/home/u2195/Desktop/Dropbox/Bioinformatics_projects/data/70aadata.txt","r")
datalist = list()
for line in f:
	newline = line.strip()
	datalist.append (newline)
titlelist = list ()
seqlist = list()
for i in datalist [:: 3]:
	titlelist.append (i)
for i in datalist[1::3]:
	seqlist.append (i)
count = 0
for i in titlelist:
	f=open('//home/u2195/Desktop/Dropbox/Bioinformatics_projects/psiblast/fastafiles'+ '/' + i + '.fasta', 'w')
	f.write(i+'\n')
	f.write(seqlist[count]+'\n')
	f.close()
	count=count+1

