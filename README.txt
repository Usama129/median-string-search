
Included scipts can execute a bounded median string search for a pattern of specified length among a set of DNA sequences.

To run, please start a command-line in this folder and type:

python main.py input.txt

Prior to running the above command, input.txt must be placed in this folder. input.txt must have the following format:

3
GACATAATCCCTA
CGCCCATCTTCTA
CACCCGTCTCTGT
GGGTCCAGTTCAA
GTGCTCGGAGAGC

The above sample input specifies a pattern length of 3 followed by 5 sequence chains.

The output is a consensus string of the specified pattern length.

After running, the output will be written to a new output.txt
