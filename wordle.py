
import random

def main():
    # main game engine

    # max number of guesses: 6
    guesses = 6

    # get words from words list
    words_list = get_words_list()

    # get random word from word list
    target_word = get_random_word(words_list)

    for i in range(guesses):
        # get user input
        guess = get_input()

        # start with an empty string to build for displaying in the output
        output_string = ""

        # go through each character in the input  
        for j in range(5):
            user_character = guess[j]
            target_character = target_word[j]

            # check to see if the user character matches the target character
            if check_match(user_character, target_character):
                output_string += make_green(user_character)
            elif check_exists(user_character, target_word):
                output_string += make_yellow(user_character)
            else:
                output_string += user_character
                
        print(output_string)
        if check_win(guess, target_word):
            print("You win!!!")
            return
        
    print("You lose")
    return



def get_words_list():
    # return the list of words from the wordle-answers.txt file as a list of words (strings)
    f = open("wordle-answers.txt", "r")
    file_contents = f.read().upper()

    return file_contents.split()

def get_random_word(words_list):
    # return random word from a list of words
    return random.choice(words_list)

def get_input():
    # return input from user.
    invalid = True
    
    while invalid:
        user_input = input("Guess a 5 letter word: ")
        if len(user_input) == 5 and user_input.isalpha():
            invalid = False
            
    return user_input.upper()

def check_match(character_1, character_2):
    # check to see if two characters match. If so: return True, if not: return False
    return character_1 == character_2

def check_exists(character, string):
    # check to see if the character exists in the string. If so: return True, if not: return False

    return character in string

def check_win(word_1, word_2):

    return word_1 == word_2





def make_yellow(c):
    return "\033[33m{}\033[0m".format(c)

def make_green(c):
    return "\033[32m{}\033[0m".format(c)

if __name__ == "__main__":
    main()