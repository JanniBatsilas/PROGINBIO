# imports
import pytest
from pathlib import Path
import os

from src.parse_fasta import parse_fasta
from src.parse_fasta import discard_ambiguous_seqs
from src.parse_fasta import nucleotide_frequencies
from src.parse_fasta import map_reads

"""
This script is to test the functionalities of parse_fasta.py
"""


def test_read_file_corectly_parse_fasta():
    """ Tests if FASTA-files are correctly parsed """

    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "files_for_testing\sequencesfasta_test.sec"
    abs_file_path = os.path.join(script_dir, rel_path)

    tup = parse_fasta(Path(abs_file_path))
    assert tup[0][0] == "sequence1"
    assert tup[0][1] == "sequence2"
    assert tup[0][2] == "sequence3"
    assert tup[0][3] == "sequence4"

    assert tup[1][0] == "GAAGTTTACTAaCTGGAGTGGTCAGaAGTTGCCGCCTGTG"
    assert tup[1][1] == "GCCCGGGCGTATGTATGAGAGATGTGGCCAGAAGTCGAAA"
    assert tup[1][2] == "ATGATTDATGTGTCCGGTAACTATAAACGTGCTACGATGT"
    assert tup[1][3] == "TTTGAG"


def test_wrong_input_parse_fasta():
    """ Tests wrong inputs to parse_fasta() """

    with pytest.raises(OSError):  # and we make sure that Python complains if we give integer instead of Path
        tup = parse_fasta(65)
    with pytest.raises(OSError):  # and we make sure that Python complains if we give integer instead of Path
        tup = parse_fasta("lol")
    with pytest.raises(TypeError):  # and we make sure that Python complains if we give integer instead of Path
        tup = parse_fasta(["wait", "this", "is", "a", "list"])


def test_discard_ambiguous_seqs():
    """ Tests if werong sequences are deleted when passed to discard_ambiguous_seqs()"""

    seq = discard_ambiguous_seqs(["ATGC", "ADGC", "GCAT", "ThE Cat LiKes Fish", "aTgC"])
    assert seq == ["ATGC", "", "GCAT", "", "ATGC"]


def test_nucleotide_frequencies(capfd):
    """ Test if print of nucleotide_frequencies is correct """

    freqs = nucleotide_frequencies(["AAA", "TTT", "GGG", "CC"])
    out, err = capfd.readouterr()
    assert "".join(out.replace('\n', "").replace(' ', "")) == "A: 0.27 C: 0.18 G: 0.27 T: 0.27".replace(" ", "")


def test_map_reads():
    """ Tests if map_read() finds sequences at correct index """

    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path1 = "files_for_testing\sequencesfasta_test.sec"
    query = os.path.join(script_dir, rel_path1)
    rel_path2 = "files_for_testing\genomefasta_test.sec"
    ref_seqs = os.path.join(script_dir, rel_path2)

    mapped_dict = map_reads(query, ref_seqs)
    assert mapped_dict['sequence1']['chr1'] == [759]
    assert mapped_dict['sequence2']['chr2'] == [1422]
    assert mapped_dict['sequence4']['chr2'] == [1039]
    assert mapped_dict['sequence4']['chr3'] == [1422]
    assert mapped_dict['sequence4']['chr4'] == [1455]


if __name__ == '__main__':
    test_map_reads()
    test_nucleotide_frequencies()
    test_discard_ambiguous_seqs()
    test_wrong_input_parse_fasta()
    test_read_file_corectly_parse_fasta()
