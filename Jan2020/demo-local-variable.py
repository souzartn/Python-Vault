##########################################################################
# Demo 
# Learn:  local variables and global variables
##########################################################################
import random
import os

#  Global Variables 
#  A variable declared outside of the function or in global scope is known as global variable. 
#  This means, global variable can be accessed inside (READ ONLY) or outside of the function.
globalVariableA=100

def ClearScreen():
    os.system('cls')
    return

def MyFunctionLocalVariable():
    # Local Variables:
    # we declare a variable inside the function to create a local variable.
    localVariableX=555
    print("@ MyFunction => variableB is:", localVariableX)
    return

def MyFunctionReadGlobalVariable():
    total = globalVariableA + 25
    print("@ MyFunctionLocal => variableA value is:", total)
    return

def MyFunctionErrorChangeGlobalVariable():
    globalVariableA = globalVariableA + 30 #ERROR: Python treats variableA as a "Local variable" and variableA is also a "Global variable"
    print("@ MyFunctionError => variableA Value is:", globalVariableA)
    return

def MyFunctionChangeGlobalVariable():
    global globalVariableA # Use "global" to indicate to Python you want to "modify" the global variable "variableA" in our function
    localVariableX=33
    globalVariableA = globalVariableA + localVariableX
    print("@ MyFunctionError => variableA Value is:", globalVariableA)


## ----------- Main program -----------
ClearScreen()

# - Test global and local variables -
print("==> Starting...variableA:",globalVariableA)
MyFunctionLocalVariable()
MyFunctionReadGlobalVariable()

#Uncomment for testing...
#MyFunctionErrorChangeGlobalVariable()
#print("==>At the End, localVariableX:",localVariableX) #ERROR "localVariableX" is a "Local variable" defined inside of functions...

print("==>After executing functions variableA:",globalVariableA)
MyFunctionChangeGlobalVariable()
print("==>At the End, after 'MyFunctionLocalAndGlobal()'  variableA:",globalVariableA)