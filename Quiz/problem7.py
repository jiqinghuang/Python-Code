def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    if n == 0:
        return True
    for i in (6, 9, 20):
        if n >=i and McNuggets(n-i):
            return True
    return False
        
    
    
