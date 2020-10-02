# This program opens a textfile, stores the words in a sorted list,
# and removes any repetitions.

FILENAME = "romeo.txt"

def main():
    with open(FILENAME, "rt") as txt_file:
        wordList = []
        for row in txt_file:
            row = row.rstrip()
            row = row.split()
            wordList += row
        # Converting to set removes duplicate words
        wordList = set(wordList)
        # Convert back to a list
        wordList = list(wordList)
        wordList.sort()
        print(wordList)
        
main()
