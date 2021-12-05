"""
parse_fasta() takes a path to a FASTA file as input and returns a tuple of two lists,
the first containing sequence headers stripped of the leading >, and the second containing the actual
sequences.
"""

from pathlib import Path
import numpy as np
import re

def map_reads(genomes, sequences):
    g_tup = parse_fasta(genomes)
    s_tup = parse_fasta(sequences)
    s_tup_clean = discard_ambiguous_seqs(s_tup[1])
    print("Short read sequences uncleaned(queries):")
    nucleotide_frequencies(s_tup[1])
    print("Short read sequences cleaned(queries):")
    nucleotide_frequencies(s_tup_clean)
    print("Reference sequences:")
    nucleotide_frequencies(g_tup[1])

    index = np.where(np.array([i != "" for i in s_tup_clean]))[0]
    d = {}
    for i in index:
        d[s_tup[0][i]] = {}
        for j in range(len(s_tup[1])):
            list = [m.start() + 1 for m in re.finditer(s_tup[1][i].upper(), g_tup[1][j])]
            if len(list) > 0:
                d[s_tup[0][i]].update({g_tup[0][j]: list})
    print("Great Success! dict was created...")
    return d


def nucleotide_frequencies(mystr):
    concatted = ''.join(mystr)
    leng = len(concatted)
    print("FUNCTION: NUCLEOTIDE FREQUENCIES")
    print("A: ", round((concatted.count("a") + concatted.count("A"))/leng, 2))
    print("C: ", round((concatted.count("c") + concatted.count("C"))/leng, 2))
    print("G: ", round((concatted.count("g") + concatted.count("G"))/leng, 2))
    print("T: ", round((concatted.count("t") + concatted.count("T"))/leng, 2))


def discard_ambiguous_seqs(sequences):
    print("FUNCTION: DISCARD AMBIGUOUS")
    allowed = "ATGCatgc"
    only_corect_seqs = []
    for i in range(len(sequences)):
        if all(c in allowed for c in sequences[i]):
            only_corect_seqs.append(sequences[i].upper())
        else:
            only_corect_seqs.append("")
    return only_corect_seqs


def parse_fasta(inputfile):
    print("FUNCTION: PARSE FASTA Processing in...", str(inputfile)[-22:])
    headers = []
    sequences = []
    string = ""

    with open(inputfile, "r", encoding='utf8') as input:
        for line in input:
            if line[0] == ">":
                headers.append(line[1:].strip())
                if len(headers) <= 1:
                    pass
                else:
                    sequences.append(string)
                    string = ""
            else:
                string = string + line.strip()

    sequences.append(string)
    return headers, sequences


if __name__ == '__main__':

    #    A 1.1    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    path1 = r"C:\Users\Janni Batsilas\Dropbox\Dokumente\01_UNI\0_Programming_in_Bio\RNA-Sequencing\Test Files\genomefasta.sec"
    genomes = Path(path1)
    tup = parse_fasta(genomes)

    #    A 1.2    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    path2 = r"C:\Users\Janni Batsilas\Dropbox\Dokumente\01_UNI\0_Programming_in_Bio\RNA-Sequencing\Test Files\sequencesfasta.sec"
    sequences = Path(path2)
    tup = parse_fasta(sequences)

    #    A 1.3    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    seqs = tup[1]
    clean = discard_ambiguous_seqs(seqs)
    nucleotide_frequencies(clean)

    #    A 1.4    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    print(map_reads(path1, path2))
