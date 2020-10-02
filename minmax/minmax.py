# Stores input number in a list, and prints out the
# maximum and minimum number

import sys

def main():
    numList = []
    while True:
        n = input("Enter a number: ")
        if n == "done":
            break;
        try:
            n = int(n)
        except:
            print("Please input integers only!")
            continue
        numList.append(n)
    print("Maximum: ", max(numList))
    print("Minimum: ", min(numList))

main()
