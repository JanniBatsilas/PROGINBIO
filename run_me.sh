#!/bin/bash

python src/execute_tasks.py
flake8 src/
coverage run --source src/ -m pytest && coverage report -m

mkdir gen1
STAR --runThreadN 4 --runMode genomeGenerate --genomeDir gen1 --genomeFastaFiles Mus_musculus.GRCm38.dna_rm.chr19.fa --sjdbGTFfile Mus_musculus.GRCm38.88.chr19.gtf --genomeSAindexNbases 11
STAR --runThreadN 4 --genomeDir gen1 --readFilesIn reads.mate_1.fq reads.mate_2.fq

grep "^@" -v Aligned.out.sam | grep "^$" -v | wc -l





