import sys

file = input("Enter the file name: ")
try:
    fhand = open(file, "rt")
except:
    print(f"File cannot be opened: {file}")
    sys.exit(-1)

with open(file, "rt") as txt_file:
    count = 0
    val = 0
    for row in txt_file:
        if not row.startswith("X-DSPAM-Confidence:"):
            continue
        count += 1
        row = row.rstrip()
        fIndex = row.find(':')
        val += float( row[fIndex+1:] )
        
print(val / count)
        
