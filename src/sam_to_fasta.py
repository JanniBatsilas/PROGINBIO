import os
from pathlib import Path
from src import parse_fasta
# import parse_fasta


def sam_to_fasta(infile: Path):
    """ converts a SAM file to a FASTA file

    This function takes the path to a SAM-file (Output of star-aligner) and produces a FASTA file from it.

    Args:
        infile : Path to SAM-File

    Returns:
        Was_once_a_sam.fa : FASTA file produced from SAM-file
    """
    outfile = Path(__file__).parents[1] / "results/was_once_a_sam.fa"
    with open(outfile, "w", encoding='utf8') as output:
        with open(infile, "r", encoding='utf8') as inp:
            for line in inp:
                if line[0] != "@":
                    try:
                        list_line = line.split("\t")
                        if list_line[9][0] == "A" or list_line[9][0] == "T" or list_line[9][0] == "G" or list_line[9][0] == "C":
                            output.write(">" + list_line[0] + "\n")
                            output.write(list_line[9] + "\n")
                    except IndexError:
                        print("Defect Line in SAM-File detected")


if __name__ == '__main__':

    #    2.2    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "/Aligned.out.sam"
    abs_file_path = script_dir + rel_path
    sam_to_fasta(Path(abs_file_path))

    queries = script_dir + "/Was_once_a_sam.fa"
    gene = script_dir + "/Mus_musculus.GRCm38.dna_rm.chr19.fa"
    dic = parse_fasta.map_reads(Path(queries), Path(gene))
    print(dic)



