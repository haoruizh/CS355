# WRITE YOUR NAME and YOUR COLLABORATORS HERE

#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the HELPER FUNCTIONS to push and pop values on the opstack 
# Remember that there is a Postscript operator called "pop" so we choose 
# different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

def opPop():
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.
    if len(opstack)>0:
        popOp = opstack[-1]
        del opstack[-1]
        return popOp
    else:
        return None

def opPush(value):
    opstack.append(value)

#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to 
# define name, and to lookup a name

def dictPop():
    # dictPop pops the top dictionary from the dictionary stack.
    popDic = dictstack[-1]
    del dictstack[-1]
    return popDic
    
def dictPush(d):
    #dictPush pushes the dictionary ‘d’ to the dictstack. 
    #Note that, your interpreter will call dictPush only when Postscript 
    #“begin” operator is called. “begin” should pop the empty dictionary from 
    #the opstack and push it onto the dictstack by calling dictPush.
    dictstack.append(d)

def define(name, value):
    #add name:value pair to the top dictionary in the dictionary stack. 
    #Keep the '/' in the name constant. 
    #Your psDef function should pop the name and value from operand stack and 
    #call the “define” function.
    newDic={name:value}
    dictstack.append(newDic)

def lookup(name):
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, 
    # but should give an appropriate error message.
    stackName = "/"+name
    for i in dictstack[::-1]:
        if stackName in i:
            return i[stackName]

#--------------------------- 10% -------------------------------------
# Arithmetic, comparison, and boolean operators: add, sub, mul, eq, lt, gt, and, or, not 
# Make sure to check the operand stack has the correct number of parameters 
# and types of the parameters are correct.
def add():
    if len(opstack) >= 2:
        op1 = opPop()
        op2 = opPop()
        if(type(op1) == int and type(op2) == int):
            opPush(op1+op2)
        else:
            print("Error: at least one operand type is not numerical")
            opPush(op2)
            opPush(op1)
    else:
        print("Error: expects 2 operands but only 1 find")


def sub():
    if len(opstack) >= 2:
        op1 = opPop()
        op2 = opPop()
        if(type(op1) == int and type(op2) == int):
            opPush(op2-op1)
        else:
            print("Error: at least one operand type is not numerical")
            opPush(op2)
            opPush(op1)
    else:
        print("Error: expects 2 operands but only 1 find")


def mul():
    if len(opstack) >= 2:
        op1 = opPop()
        op2 = opPop()
        if(type(op1) == int and type(op2) == int):
            opPush(op1*op2)
        else:
            print("Error: at least one operand type is not numerical")
            opPush(op2)
            opPush(op1)
    else:
        print("Error: expects 2 operands but only 1 find")

def eq():
    if len(opstack) >= 2:
        op1 = opPop()
        op2 = opPop()
        if(op1 == op2):
            opPush(True)
        else:
            opPush(False)
    else:
        print("Error: expects 2 operands but only 1 find")


def lt():
    if len(opstack) >= 2:
        op1 = opPop()
        op2 = opPop()
        if(type(op1) == int and type(op2) == int):
            if(op2 < op1):
                opPush(True)
            else:
                opPush(False)
        else:
            print("Error: at least one operand type is not numerical")
            opPush(op2)
            opPush(op1)
    else:
        print("Error: expects 2 operands but only 1 find")

def gt():
    if len(opstack) >= 2:
        op1 = opPop()
        op2 = opPop()
        if(type(op1) == int and type(op2) == int):
            if(op2 > op1):
                opPush(True)
            else:
                opPush(False)
        else:
            print("Error: at least one operand type is not numerical")
            opPush(op2)
            opPush(op1)
    else:
        print("Error: expects 2 operands but only 1 find")

def psAnd():
    if len(opstack) >= 2:
        op1 = opPop()
        op2 = opPop()
        if(type(op1) == bool and type(op2) == bool):
            if op2 == op1 == True:
                opPush(True)
            else:
                opPush(False)
        else:
            print("Error: at least one operand type is not boolean")
            opPush(op2)
            opPush(op1)
    else:
        print("Error: expects 2 operands but only 1 find")

def psOr():
    if len(opstack) >= 2:
        op1 = opPop()
        op2 = opPop()
        if(type(op1) == bool and type(op2) == bool):
            if op1 == True or op2 == True:
                opPush(True)
            else:
                opPush(False)
        else:
            print("Error: at least one operand type is not boolean")
            opPush(op2)
            opPush(op1)
    else:
        print("Error: expects 2 operands but only 1 find")

def psNot():
    if len(opstack) >= 1:
        op1 = opPop()
        if type(op1) == bool:
            if op1 == False:
                opPush(True)
            else:
                opPush(False)
        else:
            print("Error: at least one operand type is not boolean")
            opPush(op1)
    else:
        print("Error: expects 1 operands but only 0 find")

#--------------------------- 25% -------------------------------------
# Array operators: define the string operators length, get, getinterval, put, putinterval
def length():
    opPush(len(opPop()))

def get():
    index = opPop()
    pushedList = opPop()
    if index < len(pushedList):
        opPush(pushedList[index])
    else:
        print("Error: index out of range.")

def getinterval():
    secondIndex = opPop()
    firstIndex = opPop()
    curList = opPop()
    opPush(curList[firstIndex : secondIndex+firstIndex])

def put():
    expectValue = opPop()
    index = opPop()
    curList = opPop()
    if index < len(curList):
        curList[index] = expectValue
    else:
        print("Error: Given index out of range.")

def putinterval():
    interval = opPop()
    startIndex = opPop()
    array = opPop()
    if startIndex < len(array):
        for i in interval:
            array[startIndex] = i
            startIndex += 1
    else:
        print("Error: Given index out of range.")


#--------------------------- 15% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, count, pop, clear, exch, mark, cleartomark, counttotmark
def dup():
    if len(opstack)>0:
       top = opPop()
       opPush(top)
       opPush(top)
    else:
        print("Error: Expect at least 1 elements in stack but only find 0 element")

def copy():
    #take the value of given count
    copyCount = opPop()
    if copyCount <= len(opstack):
        #if the copyCount is in the range of length of the stack
        reverseCount = 0 - copyCount
        copyList = opstack[reverseCount:]
        for i in copyList:
            opPush(i)
    else:
        #otherwise
        print("Error: out of index")

def count():
    opPush(len(opstack))

def pop():
    opPop()

def clear():
    while len(opstack)>0:
        opPop()

def exch():
    if len(opstack) >= 2:
        elem1 = opPop()
        elem2 = opPop()
        opPush(elem1)
        opPush(elem2)
    else:
        print("Error: Expect at least two elements in stack but only find 1 or less element")

def mark():
    opPush("-mark-")

def cleartomark():
    while len(opstack)>0 and opPop() != "-mark-":
        continue

def counttomark():
    count = 0
    for i in opstack[::-1]:
        if i != "-mark-":
            count += 1
        else:
            break
    opPush(count)

def stack():
    for i in opstack[::-1]:
        print(i)

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

def psDict():
    opPush({})

def begin():
    #pop out the dict keyword
    opPop()
    dictSize = opPop()
    newDict = dict.fromkeys(set(range(dictSize)))
    dictPush(newDict)

def end():
    dictPop()

def psDef():
    value = opPop()
    variable = opPop()
    define(variable, value)
