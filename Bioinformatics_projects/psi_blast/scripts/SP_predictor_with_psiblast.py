#Extract the data from PSSM 
import numpy as np
import os
import sys
import time
from sklearn import svm 
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

f='/home/u2195/Desktop/Dropbox/Bioinformatics_projects/data/predict.fasta'
input_seq = open (f, 'r')

start_time='Starting prediction: ', time.strftime ('%Y-%m-%d, %H:%M:%S')
print(start_time)

window = 35
half_window = 17

cmd = """
#Change directory to uniref50. 
export BLASTDB=/local_uniref/uniref/uniref50

#"safety step" to check if the files have been created already in the output directory in case that the computer shuts down or others
if [ ! -f {seq}.pssm ] ; then
	echo "Running psiblast on {seq} at $(date)..."
	time psiblast -query {seq} -db uniref50.db -num_iterations 3 -evalue 0.001 -out {seq}.psiblast -out_ascii_pssm {seq}.pssm -num_threads 8
	echo "Finished running psiblast on seq at $(date)."
	echo ""
fi
#The following will be printed when the iterations are done:
echo 'PSI-BLAST run is complete'
""".format(seq=f)
os.system(cmd)

g = open(f+'.pssm')
g = g.read().splitlines()
datalist = list()
for line in g:
	newline = line.strip()
	datalist.append (newline)
titlelist = list ()
for i in datalist [:: 3]:
	titlelist.append (i)

#Define window size
window = 35
pad_size = 17

bigwordlist=[]
structvectorlist=[]

#Open all the fastafiles that are in the titlelist
for r in titlelist:
	line_list =[]
	for line in g[3:-7]:
		newline = line.split()
		newline = newline [22:42]
		line_list.append (newline)

		
#Normalize the values because they are in percentage

	for i in line_list: 
		for j in range (0, len (i)):
			i[j] = int(i[j])/100
	
#Padding, now we have vectors directly, so the padding is done by adding vectors containing 20 zeros. 
	temp_prot=[]
	a=list(np.zeros(20))
	for i in range (0, pad_size):
		temp_prot.append(a)
	temp_prot.extend(line_list)
	for i in range (0, pad_size):
		temp_prot.append(a)
		
	#print(temp_prot)
	#print(len(temp_prot))
	
#Create words with pssm information
	wordlist=[]
	for i in range (0, len (temp_prot)-(window-1)):
		b=temp_prot[i:i+(window)]
		b = [j for i in b for j in i]
		if len(b) != window*20:
			print ("oh no")
		wordlist.append(b)
	#print(wordlist)
	#print(len(wordlist))
	bigwordlist.append(wordlist)

bigwordlist=[j for i in bigwordlist for j in i]

#print (bigwordlist)
	
#print(len(bigwordlist))


#Store it in a numpy array
X = np.array(bigwordlist)


#Import the svm model 

clf = joblib.load('/home/u2195/Desktop/Dropbox/Bioinformatics_projects/results/models/psiblast_SPmodel.pkl')
predicted=clf.predict(bigwordlist)
#print(predicted)
print("This predictor has a cross-validation accuracy of 0.96")

structure_dict = { 1:'G', 2:'S'}

m=predicted.tolist()

struct_prediction=[]
for i in m:
	e = structure_dict[i]
	struct_prediction.append(e)

print (struct_prediction)

#Save the prediction output in a file 

with open ('//home/u2195/Desktop/Dropbox/Bioinformatics_projects/results/' + 'SP_Prediction_psiblast' '.fasta', 'w')as b:
	for i in range(len(titlelist)):
		b.write('Prediction of Signal Peptide using psiblast by Carolina Savatier'+'\n')
		b.write(titlelist[i]+'\n')
		b.write(''.join(struct_prediction)+'\n')

