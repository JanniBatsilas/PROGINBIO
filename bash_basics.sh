################################################################################
# Introduction to bash programming
################################################################################

# good tutorial: https://swcarpentry.github.io/shell-novice/

################################################################################

# 0. general comments
# ==============================================================================

# options/arguments are passed to the command via "-o" or "--option"
# "&" at the end of the command exectues it in the background
# many commands can be used with wildcards (globbing) (examples: "*", "?")
# get help for most commands with "man command_name"

################################################################################
# 1. basic commands
################################################################################

# list content of current direcotry
ls
ll
# list content of downstream directory
ls name/of/path
# show also hidden files
ls -a
# show all files ending with txt
ls *.txt

# make a direcotry
mkdir testing_dir
mkdir testing_dir/test_subdir

# mkdir -p testing_dir/test_subdir

# change to directory
cd testing_dir/test_subdir
# go to parent director(y/ies)
cd ../../
# go to the home directory
# cd

# copy file
cp ../exercise1/sequences.fasta testing_dir
# copy file with same name in current directory
#cp path/to/file.txt .
# copy file and change name
cp path/to/file.txt testing_dir/newName.txt

# move file
mv path/to/file.txt testing_dir/newName2.txt

# remove file
rm testing_dir/newName2.txt
# remove directory including it's content
rm -r testing_dir/test_subdir

################################################################################
# 2. important tools/programs/utilities
################################################################################

###
# print in console
###
echo "hello"
# printf "%.2f\n" 4.5667

###
# redirecting the output of commands
###
echo "This is the content of the current directory:" \
     > testing_dir/dir_content.out
ls >> testing_dir/dir_content.out

echo -e "This\nis\na\nsimple\ntextfile" \
     > testing_dir/test_file.txt
# redirecting stderr to file
rm not_existing_file.txt 2> testing_dir/error_message.err

echo -e "1\n1\n4\n5\n1\n6\n3\n4\n5\n6\n7\n8" \
     > testing_dir/example_numbers.txt

###
# cat
###
# compressed version: zcat

cat testing_dir/example_numbers.txt

###
# sort
###

sort -k1,1n testing_dir/example_numbers.txt

###
# compress
###

gzip testing_dir/example_numbers.txt

###
# uncompress
###
# ONLY if necessary
gunzip test_dir/example_numbers.txt.gz
# or also possible: gzip -d <file>

# but let's leave the file zipped
gzip test_dir/example_numbers.txt

###
# pipe
###

zcat testing_dir/example_numbers.txt.gz \
    | sort -k1,1n \
    | uniq

###
# grep
###
# compressed version: zgrep
# gives back every line of a file
# in which the search pattern ("simple" in this example) was found
grep "simple" testing_dir/test_file.txt
# inverse the output: give back all lines except for
# the ones that match the pattern
grep -v "simple" testing_dir/test_file.txt
# find lines that start with the word "This"
grep "^This" testing_dir/test_file.txt
# find lines that end with the word "a"
grep "e$" testing_dir/test_file.txt

###
# less
###
# inspect the content of a file
# (even if it is compressed)
# exit screen with "q"

# for the sake of clarity when the
# script is executed, the following command is commented out
# less testing_dir/test_file.txt

###
# pwd
###
# print your current path
pwd

###
# wc
###
# print number of words, lines, ... in a file
wc -l  testing_dir/example_numbers.txt

###
# head
###
# show first 2 lines of a file
head -n2 testing_dir/example_numbers.txt

###
# tail
###
tail -n2 testing_dir/example_numbers.txt

###
# wget
###
# download files from web (e.g. ftp server) into current directory
# for normal web sites: basic html page is downloaded (i.e. source text)


################################################################################
# 3. for loop and if-statement
################################################################################

for i in 1 2 3 4 5; do
    touch testing_dir/iterate_file_${i}.out
done

ls testing_dir/*.out

for i in testing_dir/*.out; do
    echo ${i}
    head -n1 ${i}
done

name="ralf"
if [[ ${name} == r* ]]; then
    echo "ralf, is it you?"
else
    echo "Sorry, I don't know you"
fi

for cnt in 1 5 17 10; do
    echo "current number: ${cnt}"
    if [[ -e "testing_dir/iterate_file_${cnt}.out" ]]; then
	echo "Found file"
    fi
done

n=0
for number in $(zcat testing_dir/example_numbers.txt.gz | cut -f1); do
    n=$((n+1))
    echo "In loop ${n} the number ${number} was retrieved from the input file"
done
