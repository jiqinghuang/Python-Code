'''
stuff  = 'iPad'
for thing in stuff:
    if thing == 'iPad':
        print "Found it"
'''

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x
