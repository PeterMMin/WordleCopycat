"""
Defines the Wordle game logic, including the correct word, a function to make a guess, and the main game loop.

The `makeAGuess()` function takes a user's guess as input and returns a hint string indicating which letters in the guess are correct, in the wrong position, or not in the word.

The `playWordle()` function runs the main game loop, prompting the user for guesses and printing the hint for each guess. The game continues until the user correctly guesses the word or runs out of attempts.
"""
# TASK A: Define a variable 'word' that holds the correct word for the wordle game
word= "flick"
win= ""
# TASK B: Define a function 'makeAGuess()' that passes in a users guess as a parameter
def makeAGuess(userGuess):

  # TASK C:Define a variable 'hint' that holds an empty string
  hint = ""

  # TASK D: Build a loop that loops from 0 to the length of word
  for i in range(5):

    # TASK E: Check if the current letter of guess matches the current letter of word. If so add the letter "G" to the hint
    if word[i] == userGuess[i]:
      hint+= "G"
    
    # TASK F: If the previous condition is fales, check if the current letter of guess is in word at all. If so add the letter "Y" to the hint
    elif userGuess[i] in word:
      hint += "Y"

    # TASK G: If the previous two conditions are false, add the symbol "-" to the hint
    else:
      hint += "_"
  # TASK H: Return hint
  return hint

def playWordle():
  print("Let's play wordle! /n Guess the Wordle in 6 tries. Each guess must be a valid 5-letter word. For each guess, a hint will tell you how many letters you've guessed correctly. A G represents a letter in the word and in the correct spot.. A Y represents a letter in the word but in the wrong spot. A - represents a letter not in the word in any spot. \n Guess below! \n")

  # TASK I: Build a loop that loops 6 times (representing the number of guesses a user has)
  for i in range(6):

    # TASK J: Define a variable 'guess'. prompt the user for their 5-letter guess and store it in the variable
    guess = input("What is your guess?")
    # TASK K: Define a variable 'hint' and set the return of makeAGuess(guess) to that variable
    hint= makeAGuess(guess)
    # TASK L: Print hint
    print(hint)
    # TASK M: Check if hint = "GGGGG". If so the user has won. Print a win message and break the loop
    if hint == "GGGGG":
      print("Yay you win")
      win="Y"
      return win
      break


  # TASK N: After the loop has finished, meaning the user has run out of guesses, check if hint != "GGGGG". If so, the user has lost. Print a lose message. 
  if hint != "GGGGG":
    print("You lose the word was ", word)
    win= "N"
    return win