##########################################################################
# Challenge
# Game: Create a simple hangman game.  As follows:
#   1 - Program ask master user to input a word
#   2 - Program Clear screen
#   3 - Program place an "underscore" (character '_')  for each letter of the word your guests are going to try to discover.
#   4 - Program asks Guests to call out letters, on their turn, and if the letter is in the word replacing "underscore" character by letter in correct dash space.
#   5 - If the guest calls a letter out that isn’t in the word  then you write the letter  to a list of wrong guessed letters, and inform the guest that the letter is invalid
#   6 - If the list of wrong guessed letters becomes greater than 5 - print "You lose"   
#   7 - If Guest guesses all correct letters of the word  - print "You Win"    
# Uses:  while/ for,  if,  elif, print, input,  etc
##########################################################################
import os

def ClearScreen():
    os.system('cls')
    return

HEY

print("You will NOT see this!")
ClearScreen()
print("You will  see this!")