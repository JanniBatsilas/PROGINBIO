# imports
from pathlib import Path
import os
from src.sam_to_fasta import sam_to_fasta

"""
This script is to test the functionalities of sam_to_fasta.py
"""


def test_sam_to_fasta():
    """ Tests if sam_to_fasta gives correct output with given test file """

    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "files_for_testing/sam_test.sam"
    abs_file_path = os.path.join(script_dir, rel_path)
    sam_to_fasta(Path(abs_file_path))

    with open(Path(__file__).parents[1] / "results/was_once_a_sam.fa", "r", encoding='utf8') as input:
        temp_list = []
        for line in input:
            temp_list.append(line)

    assert temp_list[0][1:9] == "NS500637"
    assert temp_list[2][1:9] == "NS500637"
    assert temp_list[4][1:9] == "NS500637"
