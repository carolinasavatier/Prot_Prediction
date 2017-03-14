#Extract the data from PSSM 
import numpy as np
import os
import sys
from sklearn import svm 
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

f = open("//home/u2195/Desktop/Dropbox/Bioinformatics_projects/data/70aadata.txt","r")
datalist = list()
for line in f:
	newline = line.strip()
	datalist.append (newline)
titlelist = list ()
structurelist = list()
for i in datalist [:: 3]:
	titlelist.append (i)
for i in datalist[2::3]:
	structurelist.append(i)

#Create a dictionary with the structures: G and S. 

structure_dict = { 'G':1, 'S':2 }

#Create a dictionary containing the protID as key and structure as value. 
ID_struct_dict = {}
for i in range (0, len(titlelist)):
	ID_struct_dict[titlelist[i]]=structurelist[i]
#print(ID_struct_dict)

#Define window size
window = int(input("window size : "))
pad_size = int(window/2)

wrongPSSMlist=[]
bigwordlist=[]
structvectorlist=[]

f=open ('/home/u2195/Desktop/Dropbox/Bioinformatics_projects/psiblast/wrongPSSM.txt', 'r')
y=f.read().splitlines()
for i in y:
	wrongPSSMlist.append(i.rstrip('.fasta'))
#print (wrongPSSMlist)
#print(len(wrongPSSMlist))
f.close()


#Open all the fastafiles that are in the titlelist
for r in titlelist:
	if (os.path.exists ('/home/u2195/Desktop/Dropbox/Bioinformatics_projects/psiblast/psiblast_data/PSSM/'+ r+'.fasta.pssm')) and (r not in wrongPSSMlist):
		d=open ('/home/u2195/Desktop/Dropbox/Bioinformatics_projects/psiblast/psiblast_data/PSSM/'+ r+'.fasta.pssm', 'r')	
		f = d.read().splitlines()
		line_list =[]
		for line in f[3:73]:
			newline = line.split()
			newline = newline [22:42]
			line_list.append (newline)
		#print (line_list)
		#print(len(line_list))

#Normalize the values because they are in percentaje

		for i in line_list: 
			for j in range (0, len (i)):
				i[j] = int(i[j])/100

#Padding, now we have vectors directly, so the padding is done by adding vectors containing 20 zeros. 
		temp_prot=[]
		a=list(np.zeros(20))
		for i in range (0, pad_size):
			temp_prot.append(a)
		#print(len([j for i in temp_prot for j in i]))
		temp_prot.extend(line_list)
		#print(len([j for i in temp_prot for j in i]))
		#print(temp_prot)
		for i in range (0, pad_size):
			temp_prot.append(a)
		#print(len([j for i in temp_prot for j in i]))
		
		#print(temp_prot)
		#print(len(temp_prot))
	
#Create words with pssm information
		wordlist=[]
		for i in range (0, len (temp_prot)-(window-1)):
			b=temp_prot[i:i+(window)]
			b = [j for i in b for j in i]
			#if len(b) != window*20:
				#print ("oh no")
			wordlist.append(b)
		#print(wordlist)
		#print(len(wordlist))
		#print(r)
		bigwordlist.append(wordlist)
		m=list(ID_struct_dict[r])
		n=[structure_dict[i]for i in m]
		structvectorlist.append(n)
		d.close()
bigwordlist=[j for i in bigwordlist for j in i]
structvectorlist=[j for i in structvectorlist for j in i]
#print (bigwordlist)
#print (structvectorlist)		
#print(len(bigwordlist))
#print(len(structvectorlist))

#Len here should be 5237 because I lost 27 proteins during the psiblast and 526 proteins give a zero pssm

#Store it in a numpy array
X = np.array(bigwordlist)
Y = np.array(structvectorlist)
#print (X, Y)

#a) Cross-validation with the function corss_val_score
'''clf=svm.LinearSVC(class_weight='balanced')
scores=cross_val_score(clf, X, structvectorlist, cv=5)
print (scores)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
clf.fit (X, structvectorlist)
predicted=clf.predict(X)
print (predicted)
sys.exit()

#b) First separate in groups  with the train_test_split function:
X_train, X_test, y_train, y_test = train_test_split(X, structvectorlist, test_size=0.20, random_state=42)'''
clf=svm.LinearSVC(C=50, class_weight='balanced')
clf.fit (X, Y) 
#predicted=clf.predict(X)
#a=accuracy_score(y_test, predicted)
#print(a)
#print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

#Save the scikit-learn model so that it can be used in the future
joblib.dump(clf, '/home/u2195/Desktop/Dropbox/Bioinformatics_projects/results/models/psiblast_SPmodel.pkl')
sys.exit()
#Confusion matrix: tn, fp, fn, tp
labels=[1, 2]
classrep=classification_report(y_test, predicted, labels=labels, digits=4)
print(classrep)
confmat=confusion_matrix(y_test, predicted, labels=labels)
print(confmat)

'''
with open ('//home/u2195/Desktop/Dropbox/Bioinformatics_projects/results/Optimization_results/' + 'classrep_confmat41' '.txt', 'w')as b:
	b.write('Window size = 25'+'\n')
	b.write(str(a)+'\n')
	b.write(str(classrep)+'\n')
	b.write(str(confmat)+'\n')
'''


