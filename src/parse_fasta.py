from pathlib import Path
import numpy as np
import re


def map_reads(sequences: Path, genomes: Path) -> dict:
    """ Reads FASTA-files, discards faulty sequences and maps occurances of substrings.

    ap_reads() takes as input two FASTA-files, the first containing short read
    sequences ("query"), and the second containing reference sequences. The function reads the files,
    discards query sequences that contain non-DNA characters, prints the nucleotide fractions for both files to
    the console and returns a dictionary of dictionaries, where the outer dictionary uses the names of query
    sequences as its keys, and the inner dictionary uses reference sequence names as keys and a list of 1-based
    indices indicating at which position (counting from left to right) in the reference sequence the query
    sequence occurs as an exact substring.

    Args:
        genomes : TList with reference sequences
        sequences : List with queries

    Returns:
        d : Dict of dicts which contain lists of indices.
    """

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


def nucleotide_frequencies(list_of_sequences: [str]):
    """ Counts frequencies and prints them to cmd

    nucleotide_frequencies() takes a list of strings as input, and prints out
    the total frequency of each nucleotide across all input sequences.

    Args:
        list_of_sequences : List of of sequences

    Returns:
        None
    """

    concatted = ''.join(list_of_sequences)
    leng = len(concatted)
    print("A: ", round((concatted.count("a") + concatted.count("A")) / leng, 2))
    print("C: ", round((concatted.count("c") + concatted.count("C")) / leng, 2))
    print("G: ", round((concatted.count("g") + concatted.count("G")) / leng, 2))
    print("T: ", round((concatted.count("t") + concatted.count("T")) / leng, 2))


def discard_ambiguous_seqs(sequences: [str]) -> [str]:
    """ Takes list of sequences and returns filtered list of the strings only containing letters (A,C,G,T)

    Takes a list of strings as input and returns only those
    strings that exclusively consist of letters of the "DNA alphabet" (A, C, G, T).
    This method does is not case sensitive.

    Args:
        sequences : List of DNA sequences

    Returns:
        only_corect_seqs : array consisting only of (A, C, G, T).
    """

    print("FUNCTION: DISCARD AMBIGUOUS")
    allowed = "ATGCatgc"
    only_corect_seqs = []
    for i in range(len(sequences)):
        if all(c in allowed for c in sequences[i]):
            only_corect_seqs.append(sequences[i].upper())
        else:
            only_corect_seqs.append("")
    return only_corect_seqs


def parse_fasta(infile: Path) -> ([str], [str]):
    """ Takes Fasta Path and returns contents in lists

    parse_fasta() takes a path to a FASTA file as input and returns a tuple of two lists,
    the first containing sequence headers stripped of the leading >,
    and the second containing the actual sequences.

    Args:
        infile : Path to Fasta-file

    Returns:
        headers : Sequence headers stripped of the leading >
        sequences : Contains the actual sequences
    """

    print("FUNCTION: PARSE FASTA Processing in...", str(infile)[-22:])
    headers = []
    sequences = []
    string = ""

    with open(infile, "r", encoding='utf8') as input:
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
    path1 = r"C:\Users\janni\Dropbox\Dokumente\01_UNI\0_Programming_in_Bio\RNA-Sequencing\Test Files\genomefasta.sec"
    # path1 = r"C:\Users\Janni Batsilas\Dropbox\Dokumente\01_UNI\0_Programming_in_Bio\RNA-Sequencing\Test Files\genomefasta.sec"
    genomes = Path(path1)
    tup = parse_fasta(genomes)

    #    A 1.2    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    path2 = r"C:\Users\janni\Dropbox\Dokumente\01_UNI\0_Programming_in_Bio\RNA-Sequencing\Test Files\sequencesfasta.sec"
    # path2 = r"C:\Users\Janni Batsilas\Dropbox\Dokumente\01_UNI\0_Programming_in_Bio\RNA-Sequencing\Test Files\sequencesfasta.sec"
    sequences = Path(path2)
    tup = parse_fasta(sequences)
    print(tup)

    #    A 1.3    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    seqs = tup[1]
    clean = discard_ambiguous_seqs(seqs)
    nucleotide_frequencies(clean)

    #    A 1.4    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    print(map_reads(path2, path1))
