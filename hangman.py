# -*- coding: utf-8 -*-
"""
Hangman

@author: Paris Klein
"""
from words import words
from words2 import words2
from words3 import words3
import random

# This function stores a list of the stages of the hangman body               
def hangman(tries):
    stages = [ """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """]
    return stages[tries]

# This function selects a word at random from words.py
def get_word1():                     
    word= random.choice(words)
    return word.upper()

def get_word2():
    word=random.choice(words2)
    return word.upper()

def get_word3():
    word=random.choice(words3)
    return word.upper()

            


# This function lets the user know if their guess was correct or incorrect.
#It also stores guesses in arrays so that the user will not guess the same letters or words again.
def game(word):
    word_length = "_" * len(word)
    guessed = False
    guessed_letters= []  
    guessed_words= []
    missed_letters=[]
    tries = 6
    print("It's time to play HANGMAN!")
    print("Please enter your first guess!")
    print (hangman(tries))
    print (word_length)
    print("\n")
    

    
    while tries > 0 and not guessed:
        guess = input("Please guess a letter or word ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter ", guess)
                
            elif guess not in word:
                print(guess, " is not in the word")
                tries -=1
                if tries ==1:
                    print("You have one try left")
                else:
                    print ("you have ", tries, " tries left")
                guessed_letters.append(guess)
                missed_letters.append(guess)
            else:
                 print("Awesome job! ", guess, " is in the word!")
                 guessed_letters.append(guess)
                 word_as_list = list(word_length)
                 indices = [i for i, letter in enumerate(word) if letter == guess]
                 for index in indices:
                     word_as_list[index] = guess
                 word_length = "".join(word_as_list)
                 if "_" not in word_length:
                    guessed = True
                    
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed this word, Please try again.")
            elif guess != word:
                print("Sorry! ",guess, " is not the answer")
                tries -=1
                if tries ==1:
                    print("you have 1 try left")
                else:
                    print("You have ", tries, " tries left")
                guessed_words.append(guess)
            else:
                guessed = True
                word_length = word
            
        else:
            print ("Not a valid guess. Please try again.")
        print(hangman(tries))
        print(word_length)
        print("\n")
        print("Missed Letters")
        print(missed_letters)
        print("\n")
    
    if guessed:
        print ("Congratulations! You guessed the word!")
        
    else:
        print("Sorry! You are out of tries. The word was " + word + ".")
                
                


#The main function
def main():
    level = int(input("what level would you like to play? (1/2/3) "))
    print(level)
    if level==1:
        word = get_word1()
        game(word)
    elif level == 2:
        word = get_word2()
        game(word)
    elif level ==3:
        word = get_word3()
        game(word)
    else:
        print("Not a valid input. Please try again")
    while input("Would you like to play again? (Y/N) ").upper() =="Y":
        return main()
        
        
        
if __name__ == "__main__":
    main()
    
