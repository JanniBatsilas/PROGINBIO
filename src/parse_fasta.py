"""
parse_fasta() takes a path to a FASTA file as input and returns a tuple of two lists,
the first containing sequence headers stripped of the leading >, and the second containing the actual
sequences.
"""

from pathlib import Path
import numpy as np


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

    index = np.where(np.array([i != "" for i in s_tup_clean]))
    index = index[0]
    d = {}
    for i in index:
        d[s_tup[0][i]] = {g_tup[0][i]: g_tup[1][i].find(s_tup[1][i])}
    return d


def nucleotide_frequencies(mystr):
    concatted = ''.join(mystr)
    leng = len(concatted)
    print("FUNCTION: NUCLEOTIDE FREQUENCIES")
    print("A: ", round((concatted.count("a") + concatted.count("A"))/leng, 3))
    print("C: ", round((concatted.count("c") + concatted.count("C"))/leng, 3))
    print("G: ", round((concatted.count("g") + concatted.count("G"))/leng, 3))
    print("T: ", round((concatted.count("t") + concatted.count("T"))/leng, 3))


def discard_ambiguous_seqs(sequences):
    print("FUNCTION: DISCARD ABIGUOUS")
    allowed = "ATGCatgc"
    discarded_list = []
    for i in range(len(sequences)):
        if all(c in allowed for c in sequences[i]):
            discarded_list.append(sequences[i].upper())
        else:
            discarded_list.append("")
    return discarded_list


def parse_fasta(inputfile):
    print("FUNCTION: PARSE FASTA Processing in...", str(inputfile)[-22:])
    headers = []
    sequences = []
    sequence_nr = 0
    ignore_1 = 0
    string = ""

    with open(inputfile, "r", encoding='utf8') as input:

        for line in input:

            if line[0] == ">":
                headers.append(line[1:].strip())
                if ignore_1 == 0:
                    ignore_1 += 1
                else:
                    sequences.append(string)
                    string = ""
                    sequence_nr += 1
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
