def chop(t):
    del t[0]
    del t[ len(t) - 1]
    return None

def middle(t):
    return t[1 : len(t) - 1]

a = [1, 2, 3, 4, 5]
chop(a)
print(a)

b = [1, 2, 3, 4, 5]
c = middle(b)
print(c)

