#######################################
# 3.1.1 INTRODUCTION TO DNA TRANSLATION
#######################################
# DNA = 1-D string of 4 Nucleotides:
#       A) Adenine
#       C) Cytosine
#       G) Guanine
#       T) Thymine
# DNA (double-stranded molecule) is transcribed into RNA (single-stranded molecule) which is translated into Proteins

# In This Case Study:
#       1) Download a DNA sequence
#       2) Translate the DNA sequence into amino acids
#       3) Download the amino acid sequence to check our solution

#   Input will be a 4-letter alphabet
#   We read as a sequence of 3 letters at a time
#   Translate each triplet into 1 letter for an amino acid
#   Proceed to the next 3 letters...

#   ATA = I
#   ATG = M
#   CAA = Q
#   TCT = S
#   TGG = W

#   Task 1: Manually download DNA and protein sequence data
#   Task 2: Import the DNA data into Python
#   Task 3: Create an algorithm to translate the DNA
#   Task 4: Check if translation matches your download

##############################################
# 3.1.1 INTRODUCTION TO DNA TRANSLATION - Quiz
##############################################
# Question 1: Which of the following is NOT a nucleotide?
# Solution 1: Lysine

# Question 2: What is the central dogma of molecular biology that describes the basic flow of genetic information?
# Solution 2: DNA -> RNA -> Protein

############################
# 3.1.2 DOWNLOADING DNA DATA
############################
# NCBI = National Center for Biotechnology Information

# We'll download 2 files from NCBI:
#       1) A Strand of DNA
#       2) A Corresponding Protein Sequence of Amino Acids

# Website = https://www.ncbi.nlm.nih.gov/nuccore/NM_207618.2

###################################
# 3.1.2 DOWNLOADING DNA DATA - Quiz
###################################
# Question 1: According to NCBI, what are the first 10 nucleotides of the gene with accession number NM_201917.1?
# Solution 1: gtaacaacca

######################################
# 3.1.3 IMPORTING DNA DATA INTO PYTHON
######################################
# Best way to read a file depends on what you want to do with it
# E.g. If you're only interested in some of the lines, use a for loop to read 1 line at a time, process/skip it, move on

# Make sure working directory contains files you want to read
pwd # pwd = Print Working Directory - We're in the right directory
# cd = Change Directory - cd 3.1_Case_Study_1_DNA_Translation/

inputfile = "dna.txt"
f = open(inputfile, "r") # r = reading
seq = f.read() # f.read is a sequence
seq # "\n" is all over the place
print(seq) # The "\n" are all gone but there are line breaks
seq = seq.replace("\n", "") # Replace "\n" with nothing and store it into new 'seq' object
seq # "\n" all gone for realsies
print(seq) # No line breaks

# There might be a "\r" object that our computer doesn't see, so just in case:
seq = seq.replace("\r", "") # Replace "\r" with nothing and store it into new 'seq' object

#############################################
# 3.1.3 IMPORTING DNA DATA INTO PYTHON - Quiz
#############################################
# Question 1: For a string text, what does the string method text.replace("X","Y") do?
# Solution 1: It is a method that creates a new string by replacing all instances of "X" in the string with "Y".

####################################
# 3.1.4 TRANSLATING THE DNA SEQUENCE
####################################
# Translation process is basically a table lookup operation
# Use a dictionary - Key = Strings of 3-letters from 4-letter alphabet; Value = Strings of 1 character
table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

table["CAA"] # Returns "Q" - Must include "" for input strings

# Step 1: Check that length of sequence is divisible by 3
    #           Do this with modulo "%"
    len(seq) # Returns "1157"
    len(seq) % 3 # Are there any remainders when dividing 1157/3 - Returns "2" - There are remainders! UH OH!

    # if len(seq) % 3 == 0: - Can use this code to make sure code only runs on sequence divisible by 3

# Step 2: Look up each 3-letter string in table and store result
    for s in seq:
        print(s) # Prints each letter in the sequence individually

    # Better to slice it into 3-letter segments
    seq[0:3] # Element 1 = "GGT"
    seq[3:6] # ELement 2 = "CAG"
    seq[6:9] # Element 3 = "AAA"
    # Need to slice to sequence 0,3,6, etc.; end point = starting point + 3 - Calls for a range object
    list(range(0, 11, 3)) # Creates a list with starting at 0, ending before 11, at a 3-step pace

    # for i in range (0, len(seq), 3):
    #   codon = seq[i : i+3]            - Can use this code to create a loop that searches for every 3-letter segment

    # Need to look up the codon & store it:
    protein = "" # Create protein list object
    protein = table[codon] # Store codon segment in protein - will need "+=" in loop to concatenate each one

# Step 3: Loop lookups until reaching end of sequence
    def translate(seq):
        # Insert code here - include creation of table object
        return protein # Return the final list of proteins
    # Also, it would be nice to include a docstring for anyone else who wants to use the function

# Code:
def translate(seq): # Define function so that it can be called using different sequences
    # Docstring
    """Translate a string containing a nucleotide sequence into a string
    containing the corresponding sequence of amino acids. Nucleotides are
    translated in triplets using the table dictionary; each amino acid
    is encoded with a string of length 1."""

    table = { # Create the 'table' dictionary in the function
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
    }
    protein = "" # Create protein list object
    if len(seq) % 3 == 0: # Check that sequence is divisible by 3
        for i in range(0, len(seq), 3): # Loop over every 3 letters
            codon = seq[i : i+3] # Create 3-letter segment
            protein += table[codon] # "+=" Concatenate the codon to protein list
    return protein # Return the final list of proteins

translate("ATA") # Returns "I" - IT WORKS!

###########################################
# 3.1.4 TRANSLATING THE DNA SEQUENCE - Quiz
###########################################
# Question 1: Use table as defined as in Video 3.1.4. The file table.py is available for download here External link as
#             well as below the video.
#             What is table["GCC"]?
# Solution 1:
table["GCC"] # Returns "A"

# Question 2: What is 138 % 13?
# Solution 2:
138 % 13 # Returns "8"

# Question 3: Open a session of Python and follow the instructions in Video 3.1.2 to read in the NCBI DNA sequence with
#             the accession number NM_207618.2 and store as seq.
#             What does seq[40:50] return?
# Solution 3:
inputfile4quiz = "dna4quiz.txt"
f4quiz = open(inputfile4quiz, "r") # r = reading
seq4quiz = f4quiz.read() # f.read is a sequence
seq4quiz = seq4quiz.replace("\n", "") # Replace "\n" with nothing and store it into new 'seq' object
seq4quiz = seq4quiz.replace("\r", "") # Replace "\r" with nothing and store it into new 'seq' object
seq4quiz[40:50] # Returns "CCTGAAAACC"

# Question 4: What is a docstring?
# Solution 4: A string that describes details about a module, function, class, or method accessed by help()

##################################
# 3.1.5 COMPARING YOUR TRANSLATION
##################################
# 'with' statement = Preferred way to read a file - it's better able to cope with situations where something goes wrong
with open(inputfile, "r") as f:
    seq = f.read()

# Create function with 'with' statement:
def read_seq(inputfile): # Define function
    # Docstring:
    """Reads and returns the input sequence with special characters removed."""
    with open(inputfile, "r") as f: # 'with' statement
        seq = f.read() # read input file
    seq = seq.replace("\n", "") # Replace "\n" with nothing and store it into new 'seq' object
    seq = seq.replace("\r", "") # Replace "\r" with nothing and store it into new 'seq' object
    return seq # Return input file as sequence

prtn = read_seq("protein.txt") # Read Protein sequence
dna = read_seq("dna.txt") # Read DNA sequence

translate(dna) # Returns "''" - Empty string - There's something wring with the length of our DNA sequence
len(dna)%3 # Returns "2"

# On website, CDS says "21..938" - We want a string that starts at 21 and ends at 938
# Sequence positions ares numbered 1 to 1157
# In Python: 21 = 20; 938 = 937 - We'll using SLICING where the stopping position is 938
translate(dna[20:938]) # There's an underscore at the very end, which we don't want
translate(dna[20:935]) # Underscore is gone!
prtn == translate(dna[20:935]) # Returns "True" - IT WORKED!!

# Alternative approach:
translate(dna[20:938])[:-1] # Eliminates underscore in amino acid sequence instead of the last 3 characters in dna
prtn == translate(dna[20:938])[:-1] # Returns "True" - IT STILL WORKS!!

#########################################
# 3.1.5 COMPARING YOUR TRANSLATION - Quiz
#########################################
# Question 1: What does the with statement do?
# Solution 1: It opens a file and uses it for the subsequent block of code only, and then closes the file.

# Question 2: Recall the final part of Video 3.1.5 regarding slicing. translate and dna are both as defined in that video.
#             What does translate(dna[20:938])[:-1] == translate(dna[20:935]) return?
# Solution 2:
translate(dna[20:938])[:-1] == translate(dna[20:935]) # Returns "True"