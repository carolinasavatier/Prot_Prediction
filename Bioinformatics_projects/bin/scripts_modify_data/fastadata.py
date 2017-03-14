import pandas as pd
#read_csv reads any kind of delimited file. csv=Comma-separated values. 

f = '/home/u2195/Desktop/Dropbox/Bioinformatics_projects/data/globular_signal_peptide_2state.txt'

data=pd.read_csv(f, header=None)

datalist=[]

for i in range (len (data)):
	if (i+1) % 3 == 0:
		datalist.extend([i])

#Drop is to remove the content of the index of the feature. #Reset index is to reset the line numbers (indexes) since they have been modified after removing a line every third line.
data.drop(data.index[datalist], inplace = True)
 
data.reset_index(drop =True, inplace =True)

data.to_csv(f + '.fasta', header= None, index = None)


