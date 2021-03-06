
## Change the following functions for static scope support. 
# dictPush
# define
# lookup
# stack


# Add a scope argument to the the following functions 
# psIf
# psIfelse
# psRepeat
# forall
# interpretSPS
# interpreter


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
    
def dictPush(d, listIndex = 0):
    #dictPush pushes the dictionary ‘d’ to the dictstack. 
    #Note that, your interpreter will call dictPush only when Postscript 
    #“begin” operator is called. “begin” should pop the empty dictionary from 
    #the opstack and push it onto the dictstack by calling dictPush.
    #initial index = 0
    #newTuple = (d, len(dictstack))
    newTuple = (d, listIndex)
    dictstack.append(newTuple)

def define(name, value):
    #add name:value pair to the top dictionary in the dictionary stack. 
    #Keep the '/' in the name constant. 
    #Your psDef function should pop the name and value from operand stack and
    #call the “define” function.
    if len(dictstack) == 0:
        dictstack.append(({}, 0))
    if name[0] != '/':
        name = '/'+name
    dictstack[-1][0][name] = value


def lookup(name, scope):
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, 
    # but should give an appropriate error message.
    if name[0] != '/':
        stackName = '/'+name
    else: 
        stackName = name
    # start lookup depend on given scope
    if scope == 'dynamic':
        for i in dictstack[::-1]:
            if stackName in i[0]:
                if isinstance(i[0][stackName], dict):
                    #if i is a code array
                    dictPush({})
                    interpretSPS(i[0][stackName], scope)
                else:
                    opPush(i[0][stackName])
                return
    elif scope == 'static':
        index = staticLink(stackName)
        if isinstance(dictstack[index][0][stackName], dict):
            #if i is a code array
            dictPush({}, index)
            interpretSPS(dictstack[index][0][stackName], scope)
        else:
            opPush(dictstack[index][0][stackName])

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
    print ("==============")
    for i in opstack[::-1]:
        print(i)
    
    length = len(dictstack)-1
    for i in dictstack[::-1]:
        print('-----'+str(length)+'---------'+str(i[1])+'--------------')
        for j in i[0].items():
            print(j)
        length -= 1
    print("==============")

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

def psDict():
    opPop()
    newDict = dict()
    opPush(newDict)

def begin():
    newDict = opPop()
    dictPush(newDict)

def end():
    dictPop()

def psDef():
    value = opPop()
    variable = opPop()
    define(variable, value)
        
#--------------------------------------------------------------------PART 2------------------------------------------------------------
import re
def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)
    


# COMPLETE THIS FUNCTION
# The it argument is an iterator.
# The tokens between '{' and '}' is included as a sub code-array (dictionary). If the
# parenteses in the input iterator is not properly nested, returns False.
def groupMatch(it):
    res = []
    for c in it:
        if c == '}':
            return {'codearray':res}
        elif c=='{':
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code-array for the inner 
            # parenthesis, it will be appended to the list we are constructing 
            # as a whole.
            res.append(groupMatch(it))
        else:
            res.append(c)
    return False



# COMPLETE THIS FUNCTION
# Function to parse a list of tokens and arrange the tokens between { and } braces 
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested dictionaries.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c=='}':  #non matching closing parenthesis; return false since there is 
                    # a syntax error in the Postscript code.
            return False
        elif c=='{':
            res.append(groupMatch(it))
        else:
            res.append(c)
    return {'codearray':res}

# COMPLETE THIS FUNCTION 
# This will probably be the largest function of the whole project, 
# but it will have a very regular and obvious structure if you've followed the plan of the assignment.
# Write additional auxiliary functions if you need them.
#handling the if operators
def psIf(scope):
    #get the code array
    codeArray = opPop()
    if opPop() is True:
        interpretSPS(codeArray, scope)

#handling the ifelse operators:
def psIfelse(scope):
    #get the code arrays
    elseCodeArray = opPop()
    trueCodeArray = opPop()
    if opPop() is True:
       interpretSPS(trueCodeArray, scope)
    else:
        interpretSPS(elseCodeArray, scope)

def forall(scope):
    commandList = opPop()
    content = opPop()
    for i in content:
        opPush(i)
        interpretSPS(commandList, scope)

def psRepeat(scope):
    codeArray = opPop()
    counter = opPop()
    while counter > 0:
        interpretSPS(codeArray, scope)
        counter -= 1    

# ------ SSPS functions -----------
# search the dictstack for the dictionary "name" is defined in and return the (list) index for that dictionary (start searhing at the top of the stack)
def staticLink(name):
    listIndex = len(dictstack)-1
    while listIndex > 0:
        if name in dictstack[listIndex][0]:
            return listIndex
        else:
            listIndex = dictstack[listIndex][1]
    return listIndex

#the main recursive interpreter function
def interpretSPS(tokenList,scope):
    commandList = tokenList['codearray']
    for i in commandList:
        if isinstance(i, dict):
            #i is a dictionary
            opPush(i)
        elif isinstance(i, str):
            #if i is a string(variable or command)
            if i[0] == '/':
                # if i initialize variable name
                opPush(i)
            elif i[0] == '[':
                opPush('[')
                newElement = ''
                result = []
                # i is a list
                content = i[1:len(i)]
                for x in content:
                    if x!=' ' and x!=']':
                        newElement += x
                    else:
                        if str.isnumeric(newElement):
                            opPush(int(newElement))
                        elif newElement == 'pop':
                            dictPop()
                        elif newElement == 'add':
                            add()
                        elif newElement == 'def':
                            #def command
                            psDef()
                        elif newElement == 'dup':
                            #dup command
                            dup()
                        elif newElement == 'mul':
                            #mul command
                            mul()
                        elif newElement == 'sub':
                            #sub command
                            sub()
                        elif newElement == 'dict':
                            #dict command
                            psDict()
                        elif newElement == 'begin':
                            #begin command
                            begin()
                        elif newElement == 'end':
                            end()
                        elif newElement =='if':
                            #if command
                            psIf(scope)
                        elif newElement == 'ifelse':
                            #ifelse command
                            psIfelse(scope)
                        elif newElement == 'forall':
                            #forall command
                            forall(scope)
                        elif newElement == "and":
                            #and command
                            psAnd()
                        elif newElement == 'eq':
                            #eq command
                            eq()
                        elif newElement == 'copy':
                            copy()
                        elif newElement == 'getinterval':
                            #getinterval command
                            getinterval()
                        elif newElement == 'putinterval':
                            putinterval()
                        elif newElement == 'exch':
                            #exchange command
                            exch()
                        elif newElement == 'get':
                            #get command
                            get()
                        elif newElement == 'repeat':
                            psRepeat(scope)
                        elif newElement == 'True' or newElement == 'true':
                            opPush(True)
                        elif newElement == 'False' or newElement == 'false':
                            opPush(False)
                        elif newElement == 'or':
                            psOr()
                        elif newElement == 'count':
                            count()
                        elif newElement == 'lt':
                            lt()
                        elif newElement == 'gt':
                            gt()
                        elif newElement == 'stack':
                            stack()
                        elif newElement == 'length':
                            length()
                        elif newElement == 'pop':
                            pop()
                        else:
                            lookup(newElement, scope)
                        newElement = ''
                for i in opstack[::-1]:
                    if i != '[':
                        result.insert(0,opPop())
                    else:
                        opPop()#pop out '['
                        opPush(result)
                        break
            elif str.isnumeric(i):
                #if i is a number
                number = int(i)
                opPush(number)
            elif i == 'def':
                #def command
                psDef()
            elif i == 'dup':
                #dup command
                dup()
            elif i == 'mul':
                #mul command
                mul()
            elif i == 'add':
                #add command
                add()
            elif i == 'sub':
                #sub command
                sub()
            elif i == 'dict':
                #dict command
                psDict()
            elif i == 'begin':
                #begin command
                begin()
            elif i == 'end':
                end()
            elif i =='if':
                #if command
                psIf(scope)
            elif i == 'ifelse':
                #ifelse command
                psIfelse(scope)
            elif i == 'forall':
                #forall command
                forall(scope)
            elif i == "and":
                #and command
                psAnd()
            elif i == 'eq':
                #eq command
                eq()
            elif i == 'getinterval':
                #getinterval command
                getinterval()
            elif i == 'putinterval':
                putinterval()
            elif i == 'exch':
                #exchange command
                exch()
            elif i == 'get':
                #get command
                get()
            elif i == 'repeat':
                #repeat command
                psRepeat(scope)
            elif i == 'True' or i == 'true':
                #bool value
                opPush(True)
            elif i == 'False' or i == 'false':
                #bool value
                opPush(False)
            elif i == 'or':
                #or command
                psOr()
            elif i =='copy':
                #copy command
                copy()
            elif i=='count':
                #count command
                count()
            elif i == 'lt':
                lt()
            elif i == 'gt':
                gt()
            elif i == 'stack':
                stack()
            elif i == 'length':
                length()
            elif i == 'pop':
                pop()
            else:
                #variable
                lookup(i, scope)

#parses the input string and calls the recursive interpreter to solve the
#program
def interpreter(s, scope):
    tokenL = parse(tokenize(s))
    interpretSPS(tokenL,scope)

#clears both stacks
def clearBoth():
    opstack[:] = []
    dictstack[:] = []








########################################################################
####  ASSIGNMENT 5 - SSPS TESTS
########################################################################

def sspsTests():
    testinput1 = """
    /x 4 def
    /g { x stack } def
    /f { /x 7 def g } def
    f
    """
    testinput2 = """
    /x 4 def
    [1 1 1] dup 1 [2 3] putinterval /arr exch def
    /g { x stack } def
    /f { 0 arr {7 mul add} forall /x exch def g } def
    f
    """
    testinput3 = """
    /m 50 def
    /n 100 def
    /egg1 {/m 25 def n} def
    /chic
    	{ /n 1 def
	      /egg2 { n stack} def
	      m  n
	      egg1
	      egg2
	    } def
    n
    chic
        """
    testinput4 = """
    /x 10 def
    /A { x } def
    /C { /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """
    testinput5 = """
    /x 10 def
    /n 5  def
    /A { 0  n {x add} repeat} def
    /C { /n 3 def /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """
    testinput6 = """
    /out true def 
    /xand { true eq {pop false} {true eq { false } { true } ifelse} ifelse dup /x exch def stack} def 
    /myput { out dup /x exch def xand } def 
    /f { /out false def myput } def 
    false f
    """
    testinput7 = """
    /x [1 2 3 4] def
    /A { x length } def
    /C { /x [10 20 30 40 50 60] def A stack } def
    /B { /x [6 7 8 9] def /A { x 0 get} def C } def
    B
    """
    testinput8 = """
    [0 1 2 3 4 5 6 7 8 9 10] 3 4 getinterval /x exch def
    /a 10 def  
    /A { x length } def
    /C { /x [a 2 mul a 3 mul dup a 4 mul] def A  a x stack } def
    /B { /x [6 7 8 9] def /A { x 0 get} def /a 5 def C } def
    B
    """

    testinput9 = """
    /x 1 def
    /g { x stack } def
    /f { /x 7 def g } def
    f
    """

    testinput10 = """
    /out false def 
    /xand { false eq {pop true} {true eq { false } { true } ifelse} ifelse dup /x exch def stack} def 
    /myput { out dup /x exch def xand } def 
    /f { /out true def myput } def 
    false f
    """

    testinput11 = """
    /x 20 def
    /A { x } def
    /C { /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """

    ssps_testinputs = [testinput1, testinput2, testinput4, testinput5, testinput6, testinput7, testinput8, testinput9, testinput10, testinput11]  #testinput3
    i = 1
    for input in ssps_testinputs:
        print('TEST CASE -',i)
        i += 1
        print("Static")
        interpreter(input, "static")
        clearBoth()
        print("Dynamic")
        interpreter(input, "dynamic")
        clearBoth()
        print('\n-----------------------------')

sspsTests()