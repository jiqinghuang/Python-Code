def search1(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
    return False

def search2(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def search3(L, e):
    def bSearch(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = low + int((high - low)/2)
        if L[mid] == e:
            return True
        if L[mid] > e:
            return bSearch(L, e, low, mid)
        else:
            return bSearch(L, e, mid+1, high)

    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L)-1)


Top = 10
for  n  in  range(1,Top+1) :
    L = range(1,n)
    print  L
    X = range(n,-1,-1)
    for  e  in  X :
        print  e, search3(L,e)
    print '=' * 20


def search4(L, e):
    # Test if the list is empty - if it is, e cannot be in it!
    # Run this test first - so that we don't throw an error trying
    #  to access L[0].
    if L == []:
        return False

    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)
