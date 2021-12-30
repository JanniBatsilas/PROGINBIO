"""
This is the main method that produces the outputs for the tasks given on the
exercise sheets.
"""
# imports
from pathlib import Path

from src import parse_fasta
from src import sam_to_fasta

# this method starts the tasks for the whole exercise (1.4 and 2.2,
# to be precise)
if __name__ == '__main__':
    """  FOLLOWING CODE PRODUCES THE OUTPUT FOR THE EXERCISE 1.4 """
    print(parse_fasta.map_reads(
        Path(__file__).parents[1] / "data/sequences.fasta",
        Path(__file__).parents[1] / "data/genome.fasta",
    ))
    """  FOLLOWING CODE PRODUCES THE OUTPUT FOR THE EXERCISE 2.2 """
    sam_to_fasta.sam_to_fasta(
        Path(__file__).parents[1] / "data/Aligned.out.sam",
    )
    dic = parse_fasta.map_reads(
        Path(__file__).parents[1] / "results/was_once_a_sam.fa",
        Path(__file__).parents[1] / "data/Mus_musculus.GRCm38.dna_rm.chr19.fa",
    )
    print(dic)
