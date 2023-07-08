#!/bin/bash

#SBATCH --job-name="hello world from openmpi 4.1.4"
#SBATCH --output="hello_world414.%j.%N.out"
#SBATCH --error="hello_world414.%j.%N.err"
#SBATCH --partition=debug
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40
#SBATCH -t 1:00:00

#module load openmpi/4.1.4/gcc-x

#mpirun --mca btl openib,vader,self \
#       --mca btl_openib_allow_ib 1 \
#        hostname


module load anaconda3
source activate Bioinfo_aditya
blastp -query Query.fasta -db database_file_name -out blastp_results_queue.tsv -evalue "evalue" -outfmt 6 -qcov_hsp_perc 50 -num_threads 40
~                                                                                  
