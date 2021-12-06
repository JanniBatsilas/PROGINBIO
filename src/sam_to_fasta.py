import os
from pathlib import Path
import parse_fasta


def sam_to_fasta(infile: Path):
    """ converts a SAM file to a FASTA file

    This function takes the path to a SAM-file (Output of star-aligner) and produces a fasta file from it

    Args:
        infile : Path to SAM-File

    Returns:
        None
    """
    outfile = "Was_once_a_sam.fa"
    with open(outfile, "w", encoding='utf8') as output:
        with open(infile, "r", encoding='utf8') as input:
            for line in input:
                if line[0] != "@":
                    list_line = line.split("\t")
                    output.write(">" + list_line[0] + "\n")
                    output.write(list_line[9] + "\n")


if __name__ == '__main__':

    #    2.2    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "/Aligned.out.sam"
    abs_file_path = script_dir + rel_path
    sam_to_fasta(Path(abs_file_path))


