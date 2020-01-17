##########################################################################
# Demo
# Learn:   variables and Function Parameters
##########################################################################
import random
import os

globalVariableA=3
globalVariableB=20

def ClearScreen():
    os.system('cls')
    return


def funtionReturn(parameterA,parameterB):
    localPower = functionPower(parameterA)
    localTotal= localPower + parameterB
    return localTotal


def functionPower(number):
    result= number * number
    return result

## ----------- Main program -----------
ClearScreen()
print ("globalVariableA: ",globalVariableA ,"globalVariableB: ",globalVariableB)
programResult= funtionReturn(globalVariableA,globalVariableB)
print ("programResult: ",programResult, " /  globalVariableA: ",globalVariableA ,"globalVariableB: ",globalVariableB)
