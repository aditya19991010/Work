#!/bin/bash

echo "To perform blastp"
echo Enter database file
read database_file



makeblastdb -in "$database_file" -dbtype prot


echo "Enter query file"
read query_file

echo "Enter E-value"
read evalue

echo "if needed add an extra command with '-', else left blank"
read command 

blastp -query "$query_file" -db "$database_file" -out blastp_results.out -evalue "$evalue" -outfmt 6
"$command"


# Check the exit status of the last command
if [ $? -eq 0 ]; then
  echo "The script completed successfully."
else
  echo "The script failed."
fi

