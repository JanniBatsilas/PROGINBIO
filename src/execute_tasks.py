# imports
from pathlib import Path
import parse_fasta
import sam_to_fasta

""" 
This is the main method that produces the outputs for the tasks given ont the exercise sheets
"""

if __name__ == '__main__':
    """  FOLLOWING CODE PRODUCES THE OUTPUT FOR THE EXERCISE 1.4 """
    print(parse_fasta.map_reads(Path("sequencesfasta.sec"), Path("genomefasta.sec")))

    """  FOLLOWING CODE PRODUCES THE OUTPUT FOR THE EXERCISE 2.2 """
    sam_to_fasta.sam_to_fasta(Path("Aligned.out.sam"))
    queries = "Was_once_a_sam.fa"
    gene = "Mus_musculus.GRCm38.dna_rm.chr19.fa"
    dic = parse_fasta.map_reads(Path(queries), Path(gene))
    print(dic)
