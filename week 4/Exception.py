def getRatios(v1, v2):
    ''' Assumes V1 and V2 are lists of equal length od numbers
        return a list containing the meaningful values of v1[i]/v2[i]'''
    ratios = []
    for index in range(len(v1)):
        try:
            ratios.append(v1[index]/float(v2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN')) # NaN = Not a Number
        except:
            raise ValueError('GetRatios callled with bad arg')
    return ratios

def traditional_get_Ratios(v1, v2):
    ''' Assumes V1 and V2 are lists of equal length od numbers
        return a list containing the meaningful values of v1[i]/v2[i]'''
    ratios = []
    if len(v1) != len(v2):
        raise ValueError('getRatios called with bad arg')
    for index in range(len(v1)):
        v1Elt = v1[index]
        v2Elt = v2[index]
        if (type(v1Elt) not in (int, float))\
           or (type(v2Elt) not in (int, float)):
            raise ValueError('getRatios called with bad arg')
        if v2Elt == 0.0:
            ratios.append(float('NaN')) # NaN = not a number
        else:
            ratios.append(v1Elt/V2Elt)
    return ratios






            
try:
    print getRatios([1.0, 2.0, 7.0, 6.0], [1.0, 2.0, 0.0, 3.0])
    print getRatios([], [])
    print getRatios([1.0, 2.0], [3.0])
except ValueError, msg:
    print msg
