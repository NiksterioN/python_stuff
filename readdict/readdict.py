
FILENAME = "words.txt"

def main():
    global wordList
    wordList = {}
    # Load the words in a dict
    with open(FILENAME, "rt") as txt_file:
        for row in txt_file:
            row = row.rstrip()
            row = row.split()
            for word in row:
                if word in wordList:
                    wordList[word] += 1
                else:
                    wordList[word] = 1
    print(wordList)
        
def searchWord(seekWord):
    if seekWord in wordList:
        return True
    else:
        return False
main()

while (w := input("Keyword: ")) != "done":
    print(searchWord(w))

