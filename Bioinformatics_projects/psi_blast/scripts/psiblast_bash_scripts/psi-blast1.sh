#After tranforming into multiple fasta files my whole dataset, run a PSI BLAST

#Change directory to uniref50. 
#id = $1
export BLASTDB=/local_uniref/uniref/uniref90
#fasta = "/home/u2195/Desktop/Dropbox/Bioinformatics_projects/psiblast/psiblast_data/fastafiles"

#for seq in *.fasta
#do
 
while read p ; do #$p is just the filename
#"safety step" to check if the files have been created already in the output directory in case that the computer shuts down or others
#if [ -f ~/Desktop/Dropbox/Bioinformatics_projects/psiblast/fastafiles/PSSM/${id}.pssm ]; then

#echo $p
	echo "Running psiblast on $p at $(date)..."
	time psiblast -query ../psiblast_data/fastafiles/$p -db uniref90.db -num_iterations 3 -evalue 0.001 -out ../psiblast_data/blastoutput/$p.psiblast -out_ascii_pssm ../psiblast_data/PSSM/$p.pssm -num_threads 8
	echo "Finished running psiblast on $seq at $(date)."
	echo ""
#fi
done <../wrongPSSM.txt

#The following will be printed when the iterations are done:
echo 'PSI-BLAST run is complete'



