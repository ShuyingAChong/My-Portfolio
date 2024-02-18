import random
import fileinput

num_letters = int(input("Enter a word length: "))
num_guesses = int(input("How many wrong answers are allowed? ")) 
word_bank = []
num_possible = [[]]
patterns_possible = [] 
indexes_checked = [] 
hidden = [] 
known = []
letters_guessed = []

for i in range(num_letters): 
    hidden.append("-") 
current = hidden

with open('dictionary.txt') as file: 
    for line in file:
        if len(line.strip()) == num_letters: 
            word_bank.append(line.strip())
print(len(word_bank))

while num_guesses > 0 and len(word_bank) > 1:
    # reset all the variables first
    patterns_possible = [] 
    num_possible = [] 
    print("You Have", num_guesses, "Guesses Left")
    print(letters_guessed) 
    print("".join(current) + "\n") 

    guess = input("Enter your guess (one letter only): ") 

    if guess in letters_guessed: # letter has already been guessed, so skip the rest of the loop and prompt again 
        print("You've already guessed " + guess + "!") 
    else: # letter not yet guessed, proceed with the loop 
        print("inside the first else!") 
        letters_guessed.append(guess)
        for word in word_bank: 
            print("checking the word!")
            for i in range(len(word)): 
                if word[i] == guess:
                    hidden[i] = guess
            pattern = "".join(hidden) # use 'hidden' to create pattern 
            if not pattern in patterns_possible: # if the pattern hasn't been seen before, add it to the list as a new pattern
                patterns_possible.append(pattern) 
                num_possible.append([word]) 
            else: # if pattern already in pattern_possible, just find the list of words w/ that pattern and add to it 
                for i in range(len(patterns_possible)): 
                    if patterns_possible[i] == pattern: 
                        break; 
                num_possible[i].append(word) 
            # we've now sorted all the words. 
            print(len(patterns_possible))
            max_possible = -1 
            max_index = -1 
            for i in patterns_possible:
                print("how many possibilities?")
                print("There are " + str(len(num_possible[i])) + " words with the pattern " + patterns_possible[i]) 
                if len(num_possible[i]) > max_possible:
                    max_possible = len(num_possible[i])
                    max_index = i

            word_bank = num_possible[max_index] 
            current = patterns_possible[max_index] # set 'current' to the final pattern
            hidden = current # set 'hidden' to final pattern, resetting for the next round 
            if not guess in current: 
                num_guesses -= 1 # decrement num_guesses because the letter wasn't in the word 
            print(current) 

word = word_bank[0] # set the word to the only remaining possible word 

while "".join(current) != word and num_guesses > 0:
    print("You have", num_guesses, "guesses left")
    print(letters_guessed)
    print("".join(current) + "\n")
    guess = input("Enter Guess: ")
    if guess in letters_guessed:
        print("You already guessed that letter, try again")
    else:
        letters_guessed.append(guess)
        num = 0 

        for i in range(len(word)):
            if word[i] == guess:
                num += 1
                current[i] = guess
                # print(hide)
        
        if guess not in word:
            print("Sorry, there are no " + str(guess) + "'s.")
            num_guesses -= 1         
        else:
            print("Yes, there is/are " + str(num) + " " + str(guess) + "'s.")
        print() # print new line divider 

if "".join(current) == word:
    print("You Win!!!")
else:
    print("You ran out of guesses!")
    print("The word was " + word)