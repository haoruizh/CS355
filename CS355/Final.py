def maxInt(L):
    maxNum = 0
    for i in L:
        if type(i) is list:
             maxNum = maxInt(i)
        else: #i is an int
            maxNum = max(i, maxNum)
    return maxNum