#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

rand_num = random.randint(0,len(word_list) - 1)
#Could also use random.choice() but for the sake of learning/understanding the functionalitly
# behind random.choice() created my own way to get a random selection.

#1
chosen_word = word_list[rand_num]

#2
guess = input("Guess a letter in the word: ").lower()

#3
for letter in chosen_word:
    if letter == guess:
        print("correct")
    else:
        print("WRONG")