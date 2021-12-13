# PROGINBIO
Project Repository for the last Project of the Lecture series Programming in Bioinformatics

I have solved most of the tasks. I had my problems with WSL and the bash comands, thats why Exercise 2.1 is not solved.
Nevertheless, I will try to solve it again and load the solution to this git repository.
I also was not able to check my code with flake8, but I tried to code as clean as possible with the standard check.

### How to produce solutions:

I put all relevant files wich are needed to produce the output either
to the /src or /test/files_for_testing direcotry. Following files are needed to produce output:

In /src directory:
- Aligned.out.sam (Output from STAR, for Exercise 2.2)
- genomefasta.sec (For Exercise 1.4)
- sequencesfasta.sec (Also for Exercise 1.4)

In /test/files_for_testing directory (Manipulated files for testing):
- sam_test.sam 
- genomefasta_test.sec 
- sequencesfasta_test.sec 

There is one file called Was_one_a_sam.fa which occurs in the test folder and the src folder.
These files have the same name but not the same content. 

Now, to generate output simply run execute_tasks.py in the /src folder.
... Anothher way to run the code is to run the run_me.sh bash script. This script will first run the test and then execute 
the output of the exercises.

### How to test:

To run the test simply use the command py -m pytest [testfile to execute]
... Another way ti run the tests is to run the run_me.sh bash script.







