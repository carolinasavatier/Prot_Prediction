# Signal Peptide Predictor using SVM
Carolina Savatier-Dupré Bañares

Training and optimization of the predictor have been done a dataset truncated to 70 residues long sequences, since the signal peptides are in the N-terminal region. Some parameters were optimized with a 10% of this truncated dataset (original dataset contains almost 6000 proteins). 

1. Signal Peptide Predictor
  Run FINALPREDICTOR.py to obtain the S and G prediction. The output is saved in the results folder. 
  The learning has been optimized and selected the best model, which is LinearSVC and a sliding window of 35. 

2. Signal Peptide Predictor with evolutionary information
  Run script called SP_predictor_with_psiblast.py saved inside the psi_blast folder (scripts). 
  This model runs a psiblast with the input sequence and then predicts.
  
  Parser_extractor.py is the script I used to parse and extract the information from the given data and then build the model.
  
  The optimization_scripts folder contains mostly optimization scripts and other parameters calculations: window size, kernel, and      C-value, use of Grid Search for optimization, Matthews correlation coefficient, Random Forest Classification...
  
