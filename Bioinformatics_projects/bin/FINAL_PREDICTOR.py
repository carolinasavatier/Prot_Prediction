############################# SIGNAL PEPTIDE PREDICTOR ###########################################
######################### CAROLINA SAVATIER-DUPRE BANARES ########################################

import sys, re
import numpy as np
import time
from datetime import datetime
from sklearn import svm 
from sklearn import preprocessing
from sklearn.svm import LinearSVC
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

#input_seq = input ('/home/u2195/Desktop/Dropbox/Bioinformatics_projects/data/predict.fasta')
input_seq = open ('/home/u2195/Desktop/Dropbox/Bioinformatics_projects/data/predict.fasta', 'r')

input_seq = input_seq.read().splitlines()

start_time='Starting prediction: ', time.strftime ('%Y-%m-%d, %H:%M:%S')
print(start_time)

window = 35
half_window = 17

datalist=[]
titlelist=[]
seqlist=[]

#Remove line breaks and put all the data in a list (datalist)

#print (len(input_seq))

for line in range(0,len(input_seq),2):
	titlelist.append(input_seq[line])
for line in range(1,len(input_seq),2):
	seqlist.append(input_seq[line])

#print (titlelist, seqlist)

#Create words with specified window size and pad them (by adding half_window size in the ends)
wordlist = []
for i in seqlist:
	i = ((half_window)*'X')+i+((half_window)*'X')
	for j in range(0, len(i)):
		if j+(window) > len(i):
			break
		a = i[j:j+(window)]
		wordlist.append(a)

#Map the words to numbers

map_word = []
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
for i in wordlist:
	temp = []
	for j in i:
		c = aa_dict[j]
		temp.append(c)
	temp = [j for i in temp for j in i]
	map_word.append(temp)

#print(map_word)
#print(len(map_word))

#OneHotEncoder to transform the mapped proteins into vectors with a binary code
#print(len(map_word[0]))
#enc = preprocessing.OneHotEncoder(n_values=21)
#map_word= enc.fit_transform(map_word).toarray()


#Import the svm model 

clf = joblib.load('/home/u2195/Desktop/Dropbox/Bioinformatics_projects/results/models/SPmodel2.pkl')
predicted=clf.predict(map_word)
print(predicted)
print("This predictor has a cross-validation accuracy of 0.97")

#Put the output back to the features, S and G

structure_dict = { 1:'G', 2:'S'}

m=predicted.tolist()

struct_prediction=[]
for i in m:
	e = structure_dict[i]
	struct_prediction.append(e)

print (struct_prediction)

#Save the prediction output in a file 

with open ('//home/u2195/Desktop/Dropbox/Bioinformatics_projects/results/' + 'SP_Prediction' '.fasta', 'w')as b:
	for i in range(len(titlelist)):
		b.write('Prediction of Signal Peptide by Carolina Savatier'+'\n')
		b.write(titlelist[i]+'\n')
		b.write(seqlist[i]+'\n')
		b.write(''.join(struct_prediction)+'\n')







