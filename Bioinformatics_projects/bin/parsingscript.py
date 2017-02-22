#Create one big list with the whole raw data file (each line is an element of the list, so we have title1, sequence1, structure1, title2...). Then create a list with all the titles,titlelist, another with all the sequences, seqlist, and another with all the structures, structurelist)

#import pandas as pd
f = open("/home/u2195/Desktop/Bioinformatics_projects/data/test.txt", "r")
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


#Create a dictionary containing the amino acids as keys and vectors defining each aa as values.

aa_dict = { 'A':[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
			'C':[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			'D':[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
			'E':[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
			'F':[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
			'G':[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0], 
			'H':[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0], 
			'I':[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0], 
			'K':[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0], 
			'L':[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0], 
			'M':[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0], 
			'N':[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
 			'Q':[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
			'P':[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0], 
			'R':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0], 
			'S':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0], 
			'T':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0], 
			'V':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0], 
			'W':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], 
			'Y':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]} 

#Create another dictionary with the different structures I have in the file, which in my case are globular, G, and signal peptide, S. 

structure_dict = { 'G':0, 'S':1 }

#Define the window size

window = 3

#Now we need to create words with the specified windows size
wordlist = list()
for i in range (0, len (seqlist)):
	for j in range(0, (len(seqlist[i])-(window-1))):
		wordlist.append(seqlist[i][j:j+(window)])
print(wordlist)

#Create a big vector for each word and store it in a list (bigvectorlist)
bigvectorlist=list()
for i in wordlist:
	vectorlist= list()
	for j in i:
		vectorlist.extend(aa_dict[j])
	bigvectorlist.append(vectorlist)
print (bigvectorlist)	
 
#Create a list for the structure corresponding to each word


# store it in a numpy array (because it's the input format).




 #For monday: X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
#y = np.array([1, 1, 2, 2])
