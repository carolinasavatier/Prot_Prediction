#Create one big list with the whole raw data file (each line is an element of the list, so we have title1, sequence1, structure1, title2...). Then create a list with all the titles,titlelist, another with all the sequences, seqlist, and another with all the structures, structurelist)
import sys, re
import numpy as np
from sklearn import svm 
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib


f = open("//home/u2195/Desktop/Dropbox/Bioinformatics_projects/data/70aadata.txt","r")
datalist = list()
for line in f:
	newline = line.strip()
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
#Add ceros in the beggining and in the endo of each sequence because every amino acid has to ocupy a middle position in the window. For that we add the X vector, which only contains ceros. 
for i in datalist[1::3]:
	seqlist.append(int(half_window)*"X"+i+"X"*int(half_window))
for i in datalist[2::3]:
	structurelist.append (int(half_window)*"X"+i+"X"*int(half_window))

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

#1. Create windows. 
windowlist = list()
countwindowlist = 0
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
print (countbigvectorlist)
sys.exit()
#2. Create a list for the structure corresponding to each word (wordstructlist):
wordstructlist= list()
n= int((window/2))
countwordstructlist = 0 
for i in range (0, len (structurelist)):
	for j in range(0, (len(structurelist[i])-(window-1))):
		a = list(structurelist[i][j:j+(window)])
		for feature in a:
			del a[:n]
			del a[-n:]		
		countwordstructlist += 1
		wordstructlist.append(a)
#print (wordstructlist)

#List flatening (because I had a list in a list):

wordstructlist = [j for i in wordstructlist for j in i]

#print (wordstructlist)

#Create a vector (structvectorlist) for each structure-word:
structvectorlist=list()
countstructvectorlist = 0 
for i in wordstructlist:
	structvectorlist.append(structure_dict[i])
	countstructvectorlist+= 1
#print (structvectorlist)

#print (countwindowlist, countbigvectorlist, countwordstructlist, countstructvectorlist)

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
'''

#Store it in a numpy array (because it's the input format).OUTPUT1:
X = np.array(bigvectorlist)
Y = np.array(structvectorlist)
#print (X, Y)
#print (np.shape(Y))

'''
#Check accuracy in my whole data set:
clf=svm.LinearSVC(class_weight='balanced')
clf.fit (X, Y)
print(clf.score (X, Y))
'''
#There are two ways of continuing now, a) cross_val_score b)train_test_split
#a) Cross-validation with the function corss_val_score
#Crossvalidate, get the best parameter and then you run the program without running a cross-validation test
#clf=svm.LinearSVC(class_weight='balanced')
#scores=cross_val_score(clf, X, Y, cv=5)
#print (scores)
#print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

#clf.fit (X, Y)
#predicted=clf.predict(X)
#print (predicted)

#b) First separate in groups  with the train_test_split function:
X_train, X_test, y_train, y_test = train_test_split(X, structvectorlist, test_size=0.20, random_state=42)
clf=svm.LinearSVC(class_weight='balanced', C=16)
clf.fit (X_train, y_train) 
predicted=clf.predict(X_test)
a=accuracy_score(y_test, predicted)
print(a)
#print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))


#Save the scikit-learn model so that it can be used in the future
joblib.dump(clf, '/home/u2195/Desktop/Dropbox/Bioinformatics_projects/results/models/SPmodel.pkl') 

#Confusion matrix: tn, fp, fn, tp
labels=[1, 2]
classrep=classification_report(y_test, predicted, labels=labels, digits=4)
print(classrep)
confmat=confusion_matrix(y_test, predicted, labels=labels)
print(confmat)
sys.exit()
with open ('//home/u2195/Desktop/Dropbox/Bioinformatics_projects/results/Optimization_results/' + 'classrep_confmat41' '.txt', 'w')as b:
	b.write('Window size = 25'+'\n')
	b.write(str(a)+'\n')
	b.write(str(classrep)+'\n')
	b.write(str(confmat)+'\n')



