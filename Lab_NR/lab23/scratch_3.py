# A. Create two functions AddNumbers(x,y) and SubtractNumbers(x,y) that add/subtract
# the two numbers respectively. Create a function OperateNumbers that takes
# AddNumbers / SubtractNumbers as argument and invokes the function passed as
# argument with default values.
# B. Repeat the above for the operations on strings (ConcatenateStrings(str1, str2) and
# ReplaceWord(str1, str2=”” and OperateStrings(func) )
from pydoc import replace
from webbrowser import Opera


def AddNumbers(x,y):
    res = x + y
    return print(f"Addition of {x} and {y} is {res}")

def SubtractNumbers(x,y):
    res = x-y
    return print(f"Subtraction of {x} and {y} is {res}")


def OperateNumbers(func,a,b):
    func(a,b)
    return


OperateNumbers(AddNumbers,1010,1202)
OperateNumbers(SubtractNumbers,1010,800)


str1 = "Hello! "
str2 = "World"
def ConcatenateStrings(str1,str2):
    return print(str1+str2)

def ReplaceWord(str1,str2=""):
    replaced = replace(str1,str2)
    return print(replaced)

def OperateStrings(func,a,b):
    return func(a,b)

OperateStrings(ConcatenateStrings,str1,str2)
OperateStrings(ReplaceWord,str1,str2)