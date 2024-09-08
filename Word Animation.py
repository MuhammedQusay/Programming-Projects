import string
from time import sleep
from random import choice

def display_word(the_word):
    word_length = len(the_word)
    result = [''] * word_length  
    completed = [False] * word_length  
    
    while not all(completed):
        for index, letter in enumerate(the_word):
            if completed[index]: 
                continue
            
            if letter == " ":
                result[index] = " "  
                completed[index] = True
            else:
                result[index] = choice(string.ascii_lowercase)
                if result[index] == letter.lower():
                    completed[index] = True  

        print("".join(result), end="\r")  
        sleep(0.05)

    print("".join(result))  

if __name__ == "__main__":
    the_word = input("Write a word: ")
    display_word(the_word)
