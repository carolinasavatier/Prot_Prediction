import os
import numpy as np
import sys
f = '/home/u2195/Desktop/Dropbox/Bioinformatics_projects/psiblast/psiblast_data/PSSM/'

titlelist = list ()

titlelist = os.listdir(f)

wrongtitle_list = []

for r in titlelist:
	if os.path.exists ('/home/u2195/Desktop/Dropbox/Bioinformatics_projects/psiblast/psiblast_data/PSSM/'+ r):
		#print("Testing file with name %s"%(r))
		d=open ('/home/u2195/Desktop/Dropbox/Bioinformatics_projects/psiblast/psiblast_data/PSSM/'+ r, 'r')	
		f = d.read().splitlines()
		newline3 =[]
		
		for line in f[3:73]:
			newline = line.split()
			newline2 = [int(item) for item in newline[22:42]]
			newline3.extend(newline2)
		if np.array(newline3, dtype=int).any() == np.zeros(len(newline3), dtype=int).any():
			a=r.replace('.pssm', '')			
			wrongtitle_list.append(a)
			
#print (wrongtitle_list)

with open ('//home/u2195/Desktop/Dropbox/Bioinformatics_projects/psiblast'+ '/' + 'wrongPSSM' + '.txt', 'w')as b:
	for i in range(0, len (wrongtitle_list)):
		b.write(wrongtitle_list[i]+'\n')
		#b.write(str(len(wrongtitle_list))+'\n')
		b.close
		
