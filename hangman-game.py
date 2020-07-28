#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Kshitiz Bhandari
"""
import random
import string


def welcome():
    '''
    Prints the name of the game and welcomes the user
    '''
    print('''
     _   _                                          
    | | | |                                         
    | |_| | __ _ _ ___  __ _ _ __ ____  __ _ _ ___  
    |  _  |/ _` | '_  \/ _` | '_ ` _  \/ _` | '_  \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | | 
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                        __/ |                       
                       |____/                           
    ''')
    print('Welcome to the game, Hangman!')


def gameStatus(life_left):
    '''
    Assumes life_left is an integer between 1 and 8

    Returns strings which when printed represent pictorial status of the hangman game. 
    '''
    assert 1 <= life_left & life_left <= 8, "Invalid number of lives"
    
    HANGMAN_PICS = ['''                
     +---+
     |   |
     O   |
    /|\  |
    / \  |
        ===''', '''
     +---+
     |   |
     O   |
    /|\  |
    /    |
        ===''', '''
     +---+
     |   |
     O   |
    /|\  |
         |
        ===''', '''
     +---+
     |   |
     O   |
    /|   |
         |
        ===''', '''
     +---+
     |   |
     O   |
     |   |
         |
        ===''', '''
     +---+
     |   |
     O   |
         |
         |
        ===''', '''
     +---+
     |   |
         |
         |
         |
        ===''','''
     +---+
         |
         |
         |
         |
        ===''']

    return HANGMAN_PICS[life_left - 1]


 
def gameWon():
    '''
    Returns graphic for when the user wins the game
    '''
    return '''
                 *     ,MMM8&&&.            *      
                      MMMM88&&&&&    .             
                     MMMM88&&&&&&&                 
         *           MMM88&&&&&&&&                 
                     MMM88&&&&&&&&                 
                     'MMM88&&&&&&'                 
                       'MMM8&&&'      *    _     
        '     |\___/|                      \\    
             =) ^Y^ (=   |\_/|             ||  '   
              \  ^  /    )a a '._.------.  //      
               )===(    =\T_= /    ~  ~  \//       
              /     \     ` `\   ~   / ~  /        
              |     |         |~   \ |  ~/         
             /| | | |\         \  ~/- \ ~\         
             \| | |_|/|        || |  // /`         
      _/\_/\_/'_/\ \_/'\_/'\_/((_/'((/'\\/'\_/\_/\_
      |  |  |   | \_)   |   |   |   |   |   |  |  |   
      |  |  | C | O | N | G | R | A | T | S |  |  |
      |  |  |   |   |   |   |   |   |   |   |  |  |
      |  |  | Y | O | U |   | W | O | N | ! |  |  |
      |  |  |   |   |   |   |   |   |   |   |  |  |
    '''



def gameLost():
    '''
    Returns graphic for when the user loses the game 
        (i.e. fails to guess the word correctly)
    '''
    return '''
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀┼┼
    ┼┼██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼┼┼
    ┼┼██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀┼┼
    ┼┼██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼┼┼
    ┼┼███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼┼┼
    ┼┼██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼┼┼
    ┼┼██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼┼┼
    ┼┼██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼┼┼
    ┼┼███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼┼┼
    '''



def loadWords(filename):
    '''
    filename: string, name of a file
    Takes a file and returns a list of valid words.
        (Words are strings of lowercase letters.)
    Depending on the size of the word list, this function may take a while.
    '''
    print('Loading word list from file...')
    file = open(filename, 'r')
    # line: string
    line = file.readline()
    # wordlist: list of strings
    wordlist = line.split()
    
    print('  ', len(wordlist), 'words loaded.')
    file.close()
    
    return wordlist



def chooseWord(wordlist):
    '''
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    '''
    return random.choice(wordlist)



def isWordGuessed(secret_word, letters_guessed):
    '''
    secret_word: sring, the word that the user is trying to guess
    letters_guessed: list, what letters have been guessed so far
    Returns a boolean value:
        True if all the letters of secret_word are in letters_guessed;
        False otherwise
    '''
    test = True
    for a in secret_word:
        if a not in letters_guessed:
            test = False
            break
    return test


def getGuessedWord(secret_word, letters_guessed):
    '''
    secret_word: sring, the word that the user is trying to guess
    letters_guessed: list, what letters have been guessed so far
    
    Returns a string comprised of letters and underscores that represents what
        letters in secret_word have been guessed so far
    '''
    # initialize to keep track of word state
    s = ''
    # iterate through the word to be guessed
    for letter in secret_word:
        # include the letter if it has been guessed
        if letter in letters_guessed:
            s = s + letter + ' '
        # otherwise keep the underscore 
        # (to represent a letter space left to be filled)
        else:
            s = s + '_ '
    # return the state of the word guessed so far
    return s


def getAvailableLetters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    
    Returns a string comprised of letters that represents what letters have
        not yet been guessed
    '''
    result = ''
    # iterate through the entire alphabet (lowercase)
    for letter in string.ascii_lowercase:
        # store letters that have not yet been guessed yet
        if letter not in letters_guessed:
            result = result + letter
   
    # return the letters left to be guessed
    return result


def hangman(secret_word):
    '''
    secret_word: string, the secret word that the user has to guess

    Starts up an interactive game of Hangman
    '''
    letters_guessed = []
    life_left = 8
    
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('-----------------------------------------------')
    
    while (not isWordGuessed(secret_word, letters_guessed)) and life_left > 0:
        print(gameStatus(life_left))
        print('')
        print('You have', life_left, 'guesses left.')
        print('Available Letters:', getAvailableLetters(letters_guessed))
        # initialize with a random word
        guess = 'hangman'
        
        # Defensive programming to ensure that the user enters only one letter
        while len(guess) != 1 or guess not in string.ascii_lowercase:
            guess = input('Please guess a letter: ')
            # convert the letter to lowercase if it is not already
            guess = guess.lower()
            
            # if the guess is more than one character
            if len(guess) != 1:
                print('Please enter only one letter at a time!')
            # if the guess is not a letter
            elif guess not in string.ascii_lowercase:
                print('Please enter an actual letter!')
            # if the guess is a single letter, break out of loop
            else:
                break
        
        # if the letter has not yet been guessed
        if guess not in letters_guessed:
            # append it to the already guessed list
            letters_guessed.append(guess)
            
            # check if the new guess is in the secret word
            if guess in secret_word:
                print('Good guess:', getGuessedWord(secret_word, letters_guessed))
                print('===========')
            # if not, reduce the number of lives by 1
            else:
                # incorrect guess: update lives left
                print('Oops! That letter is not in my word:', getGuessedWord(secret_word, letters_guessed))
                print('====================================')
                life_left -= 1
       # if it is already guessed, let the user know
        else:
            print('Oops! You\'ve already guessed the letter:', getGuessedWord(secret_word, letters_guessed))
            print('=========================================')
    
    print()
    # after ending the loop: Either the user won or ran out of lives
    if isWordGuessed(secret_word, letters_guessed):
        print(gameWon())
    else:
        print(gameLost())
        print('Sorry, you ran out of guesses.\n  The word was:', secret_word)
        


if __name__ == "__main__":
    # welcome the user
    welcome()
    # load wordlist from file
    wordlist_filename = 'words.txt'
    wordlist = loadWords(wordlist_filename)
    print('')
    
    # choose a secret word from the words loaded
    secret_word = chooseWord(wordlist)
    
    # start an interactive game of hangman
    hangman(secret_word)