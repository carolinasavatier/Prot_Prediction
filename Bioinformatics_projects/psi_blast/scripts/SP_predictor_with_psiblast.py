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

os.system("""
#Change directory to uniref50. 
export BLASTDB=/local_uniref/uniref/uniref50

for seq in f.fasta
do

#"safety step" to check if the files have been created already in the output directory in case that the computer shuts down or others

if [ ! -f ~/Desktop/Dropbox/Bioinformatics_projects/psiblast/fastafiles/PSSM/$seq.pssm ]; then
	echo "Running psiblast on $seq at $(date)..."
	time psiblast -query $seq -db uniref50.db -num_iterations 3 -evalue 0.001 -out blastoutput/$seq.psiblast -out_ascii_pssm PSSM/$seq.pssm -num_threads 8
	echo "Finished running psiblast on $seq at $(date)."
	echo ""
fi
done

#The following will be printed when the iterations are done:
echo 'PSI-BLAST run is complete'
""")


