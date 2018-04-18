# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 23:11:42 2017

@author: harne
"""
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for char in secretWord:
        if char in lettersGuessed:
            count +=1
    if count == len(secretWord):
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ''
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            word += secretWord[i]
        else:
            word += "_"
            
    return word
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = string.ascii_lowercase
    available_letters = ''
    for char in letters:
        if char not in lettersGuessed:
            available_letters += char
    return available_letters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    guesses = 8
    letters_guessed = []
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long")
    while guesses > 0:
        if guesses == 0 or getGuessedWord(secretWord, letters_guessed) == secretWord:
            break
        print ("------------")
        print("You have " + str(guesses) + " guesses left.")
        print("Available letters: " + getAvailableLetters(letters_guessed))
        guess = input("Please guess a letter: ")
        if guess in letters_guessed:
            letters_guessed.append(guess)
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, letters_guessed))
        elif guess in secretWord:
            letters_guessed.append(guess)
            print("Good guess: " + getGuessedWord(secretWord, letters_guessed))
            
        else: 
            letters_guessed.append(guess)
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, letters_guessed))
            guesses -= 1
    
       
    print("------------")
    if guesses == 0:
        print("Sorry, you ran out of guesses. The word was else.")
    else:
        print("Congratulations, you won!")