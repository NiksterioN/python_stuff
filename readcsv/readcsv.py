import csv
import re
from sys import argv

CSV_FILE = "small.csv"
SEQ_FILE = "4.txt"

# Read the First Line, or Keys for search patterns
with open(CSV_FILE, "rt") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        patternDNA = row[1:]
        break;
    
patternCountDNA = dict.fromkeys(patternDNA, 0)

# Read the DNA Sequence
with open(SEQ_FILE, "rt") as seq_file:
    for dna_str in seq_file:
        seq = dna_str

# Parse the DNA Sequence for Patterns
countMax = 0;

for pattern in patternDNA:
    # Search for the first occurence
    countMax = 0
    fIndex = seq.find(pattern)

    if fIndex == -1:
        print("No pattern found!")
        break
    countCurr = 1
    # Loop Until no more occurence
    while fIndex != -1:
        # Next Occurence
        NIndex = seq.find(pattern, fIndex + len(pattern))
        # If pattern continues,
        if NIndex - fIndex == len(pattern):
            countCurr += 1
        else:
            if countCurr > countMax:
                countMax = countCurr
            countCurr = 1       
        fIndex = NIndex;

    patternCountDNA[pattern] = str(countMax)
    
# Check for similar DNA pattern counts
with open(CSV_FILE, "rt") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Skip the first row
    next(csv_reader)
    for row in csv_reader:
        countSimilar = 0;
        for pattern in patternDNA:
            if row[pattern] == patternCountDNA[pattern]:
                countSimilar += 1
            else:
                break
        if countSimilar == len(patternDNA):
            print(row.get("name"))
            break
if countSimilar < len(patternDNA):
    print("No match")
        
        
        
