#!/bin/bash

# Define an array of file names
files=(
  "SRR6660738"
  "SRR6660748"
  "SRR6660754"
  "SRR6660764"
  "SRR6660767"
  "SRR6660768"
  "SRR6660772"
  "SRR6660777"
)

# Loop through the files
for file in "${files[@]}"; do
  # Set the input and output file paths
  input_file_2="${files}_2_trim_2P.fastq"
  output_file_2="${files}_2_trim_rm_adap.fastq"
  ovrpseq="${files}_1_trim_1P.fastq_fastqc.fasta"
  
  # Run trimmomatic to remove the first 13 bases
  java -jar /home/aditya/software/Trimmomatic/trimmomatic-0.39.jar PE -threads 40 -phred33 "${input_file_1}" "${output_file_1}_1P" ILLUMINACLIP:$ovrpseq
done
