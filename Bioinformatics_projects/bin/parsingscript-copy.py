#Create one big list with the whole raw data file (each line is an element of the list, so we have title1, sequence1, structure1, title2...). Then create a list with all the titles,titlelist, another with all the sequences, seqlist, and another with all the structures, structurelist)
import sys

f = open("../data/trial.txt","r")
datalist = list()
for line in f:
	newline = line.replace ("\n", "")
	datalist.append (newline)
titlelist = list ()
seqlist = list()
structurelist = list()
window = int(input("window size : "))
half_window= float(window/2)
counttitlelist=0
for i in datalist [:: 3]:
	titlelist.append (i)
	counttitlelist +=1
for i in datalist[1::3]:
	seqlist.append (i)
for i in datalist[2::3]:
	structurelist.append(i)
#Add ceros in the beggining and in the endo of each sequence because every amino acid has to ocupy a middle position in the window. For that we add the X vector, which only contains ceros. 
#for i in datalist[1::3]:
	#seqlist.append(int(half_window)*"X"+i+"X"*int(half_window))
#for i in datalist[2::3]:
	#structurelist.append (int(half_window)*"X"+i+"X"*int(half_window))

#Create a dictionary containing the amino acids as keys and vectors defining each aa as values.

aa_dict = { 'A':[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
			'C':[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			'D':[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
			'E':[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
			'F':[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
			'G':[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
			'H':[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0], 
			'I':[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0], 
			'K':[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0], 
			'L':[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0], 
			'M':[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0], 
			'N':[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
 			'Q':[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
			'P':[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0], 
			'R':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0], 
			'S':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0], 
			'T':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0], 
			'V':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0], 
			'W':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], 
			'Y':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
			'X':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]} 

#Create another dictionary with the different structures I have in the file, which in my case are globular, G, and signal peptide, S. 

structure_dict = { 'G':1, 'S':2 , 'X':0}

#Create windows. Padd the beggining and the end of the protein
windowlist = list()
countwindowlist = 0
null_pad= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range (0, len (seqlist)):
	for j in range (0, len (seqlist[i])-(window-1)):
		windowlist.append(seqlist[i][j:j+(window)])
		countwindowlist += 1
#print (windowlist)

#Create a big vector for each word and store it in a list (bigvectorlist)
bigvectorlist=list()
countbigvectorlist = 0
for i in windowlist:
	vectorlist= list()
	for j in i:
		vectorlist.extend(aa_dict[j])
	bigvectorlist.append(vectorlist)
	countbigvectorlist += 1
print (bigvectorlist)

for i in range (len ()):
	if i  == 0:
		null_pad + prot[i] + prot[i + 1]
	elif i ==(len ()-1):

sys.exit()

#HERE IS THE ERROR. Create a list for the structure corresponding to each word (wordstructlist):
wordstructlist= list()
countwordstructlist = 0 
for i in range (0, len (structurelist)):
	for j in range(0, (len(structurelist[i])-(window-1))):
		a = list(structurelist[i][j:j+(window)])
		for feature in a:
			del a[0]
			del a[-1]		
		countwordstructlist += 1
		wordstructlist.append(a)
print (wordstructlist)

#List flatening (because I had a list in a list):

wordstructlist = [j for i in wordstructlist for j in i]

#print (wordstructlist)

#Create a vector (structvectorlist) for each structure-word:
structvectorlist=list()
countstructvectorlist = 0 
for i in wordstructlist:
	structvectorlist.append(structure_dict[i])
	countstructvectorlist+= 1
print (structvectorlist)
#print (len (vectorlist2))

#print(structvectorlist)

print (len (bigvectorlist))
print (len (structvectorlist))

print (countwordlist, countbigvectorlist, countwordstructlist, countstructvectorlist)

#Save the outputs for the svm in two files, svm_input_window and svm_input_feature 
'''
with open('../results/svm_input_window.txt', 'w') as VL:
	for i in range(0, len(bigvectorlist)):
		VL.write('\n')
		for j in bigvectorlist[i]:
			VL.write(str(j)+',')

with open('../results/svm_input_feature.txt', 'w') as VL:
	for i in range(0, len(structvectorlist)):
		VL.write(str(structvectorlist[i])+'\n')

#Store it in a numpy array (because it's the input format).OUTPUT1:
import numpy as np
X = np.array(bigvectorlist)
Y = np.array(structvectorlist)
#print (X, Y)
#print (np.shape(Y))
'''

#Cross-validation: to avoid my algorith to overfit.

from sklearn import svm 
from sklearn.model_selection import cross_val_score
clf=svm.LinearSVC()
scores=cross_val_score(clf, bigvectorlist, structvectorlist, cv=5)
print(scores)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

#Now I have the correct output to train the machine. I will use Support Vector Machine (svm), a type of  supervised Machine Learning with labelled data. We will do classification with sklearn.svm. 
#from sklearn import svm 
#clf=svm.LinearSVC()
#clf.fit (X, Y)
#print (clf.predict(X))


