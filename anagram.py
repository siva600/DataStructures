def anagramSolution4(s1,s2):  # O(n)
    """
      count and compare
    """
    c1 = [0]*26
    n = len(s1)
    x = ord('a')
    for i in range( n ):
        pos = ord(s1[i])-x
        print(pos)
        c1[pos] += 1
        pos = ord(s2[i])-x
        c1[pos] -=  1
        print(c1)
    for i in c1:
        if i != 0:
            return False

    return True


print(anagramSolution4("ebb", "edd"))