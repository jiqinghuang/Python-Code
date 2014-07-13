def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    if len(s1) >= len(s2):
        part1 = s1[:len(s2)]
        part2 = s2
        reminder = s1[len(s2):]
    else:
        part1 = s1
        part2 = s2[:len(s1)]
        reminder = s2[len(s1):]

    result  = ''
    for i in range(len(part1)):
        result = result + part1[i] + part2[i]

    result = result + reminder
    return result
    
    
