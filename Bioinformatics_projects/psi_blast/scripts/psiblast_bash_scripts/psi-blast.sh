#After tranforming into multiple fasta files my whola dataset, run a PSI BLAST

#Change directory to uniref50. 
export BLASTDB=/local_uniref/uniref/uniref50

for seq in *.fasta
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

