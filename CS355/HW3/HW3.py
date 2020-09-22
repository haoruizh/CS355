from functools import reduce
# Part 1
# Problem a sumSales
def sumSales(d):
    sumSalesD = {}
    # iterative through the first dictionary
    for K, I in d.items():
        # iterative through the second dictionary
        for k, i in I.items():
            if k in sumSalesD.keys():
                sumSalesD[k] += i
            else:
                sumSalesD[k] = i
    return sumSalesD

# problem b sumSalesN
#combine dictionaries from a list
def combineDictionaries(L):
    resultDic = {} 
    for i in L:
        for k, j in i.items():
            if k in resultDic:
                resultDic[k] += j
            else:
                resultDic[k] = j
    return resultDic
        
def sumSalesN(L):
    sumSalesDic = {}
    sumSalesDic = map(sumSales, L)
    return combineDictionaries(sumSalesDic)

# Part 2
# problem a searchDicts
def searchDicts(L, K):
    result = None
    for i in L:
        if K in i:
            result = i[K]
    return result


# problem b searchDicts2
def searchDicts2Helper(L, K, i):
    l  = L[i][1]
    if K in l.keys():
        return l[K]
    if i == L[i][0]:
        return None
    return searchDicts2Helper(L,K,L[i][0])

def searchDicts2(L, K):
    return searchDicts2Helper(L, K, len(L)-1)



# Part 3
def busStops(buses, stop):
    #if stop is in buses
    result = [i for i in buses if stop in buses[i]]
    return result


# part 4
def palindromes(S):
    result = []
    #iterative through the string twice and find all possible strings to check if it is palindromes
    #first loop
    for i in range(len(S)):
        #second loop
        for x in range(i+1, len(S)):
            if S[i:x+1] == "".join(reversed(S[i:x+1])):
                result.append(S[i:x+1])
    #remove duplicate part
    result = list(dict.fromkeys(result))
    #sort the result list
    result.sort()
    return result
                


# part 5
# problem a
class interlaceIter():
    #initial function
    def __init__(self, elem1, elem2):
        self.firstEle = elem1
        self.secondEle = elem2
        self.result = []
        for x, y in zip(self.firstEle, self.secondEle):
            self.result.append(x)
            self.result.append(y)
        self.result = iter(self.result)

    def __next__(self):
        try:
            self.current =  self.result.__next__()
        except:
            raise StopIteration
        return self.current
    
    def __iter__(self):
        return self

# problem b:
def typeHistogram(it, n):
    d = dict()
    for i in range(n):
        try:
            current = it.__next__()
            # if current type is in the dictionary
            if type(current).__name__ in d.keys():
                d[type(current).__name__] += 1
            else: # if current type is not in the dictionary
                d[type(current).__name__] = 1
        except StopIteration:
            break
    #sort d
    sorted(d.items())
    key = d.keys()
    count = d.values()
    return list(zip(list(key), list(count)))