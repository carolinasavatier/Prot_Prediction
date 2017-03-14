#Analyze the proportion of features I have in my data (G and S)
import sys
import statistics as stat
f = open("../data/70aadata.txt","r")

f = f.read().splitlines()
structureset = []
for i in range(2, len(f), 3):
	structureset.append(f[i])
total = len(structureset)
countG = 0
numberofS = []
for eachstruc in structureset:
	theset = set([i for i in eachstruc])
	if 'S' not in theset:
		countG += 1	
	if 'S' in theset:
		countS = 0
		for i in eachstruc:
			if i == 'S':
				countS += 1
		numberofS.append(countS)
print ("Proteins containing only G:", countG)
print ("Proteins containing G and S:", (total-countG))
print ("Signal peptide average lenght: ", stat.mean(numberofS))
#print (numberofS)

with open ('//home/u2195/Desktop/Dropbox/Bioinformatics_projects/results'+ '/' + 'ProtAnalysis_averageSignalPep' + '.txt', 'w')as b:
	b.write("Proteins containing only G:"+ str(countG)+'\n')
	b.write("Proteins containing G and S:"+ str(total-countG)+'\n')
	b.write("Signal peptide average lenght: " + str(stat.mean(numberofS)))
	b.close
