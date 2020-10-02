def main():
    myList = [1, 2, 3, 4, 5]
    chop(myList)
    print(myList)
    
    myList = [2, 3, 4, 5, 6]
    modList = middle(myList)
    print(modList)
# A function that passes objects by references. Directly modifies
# the input list.
def chop(t):
    # Removes the FIRST element of the list
    del t[0]
    # Removes the LAST element of the list
    del t[len(t)-1]

# Also a pass by reference, however the method generates and returns
# a modified list.
def middle(t):
    return t[1:len(t)-1]

main()
