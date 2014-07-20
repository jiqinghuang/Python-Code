def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i/10
    return result

## this is a very classic code
def addDigits(s):
    val = 0
    for c in s:
        val += int(c)
    return val

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

# quadratic polynomial complexity
def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True


def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    '''after find similaties, then delete duplicates.
    '''
    res = []
    for e in tmp:
        if not (e in res):
            res.append(e)
    return res

def genSubsets(L):
    res = []
    if len(L) == 0:
        return [[]] # list of empty list
    smaller = genSubsets(L[:-1])
    # get all subsets without last element
    extra = L[-1:]
    # create a list of just last element
    new = []
    for small in smaller:
        new.append(small+extra)
    # for all small solutions, add one with last element
    return smaller + new
    # combin those with last element and those without.



    
