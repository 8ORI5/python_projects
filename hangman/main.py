# simple implementation of hangman game

import random
import string

secret = ['PYTHON', 'java', 'kotlin', 'javascript']
word = random.choice(secret)

play = True

print("H A N G M A N")

while play:
    ascii = string.ascii_letters
    random.seed()
    answer = random.choice(secret).lower()
    current = list("-" * len(answer))
    answer_set = set(answer)
    guesses = []
    tries = 10

    play_again = input('Type "play" to play the game, "exit" to quit: ').lower()
    if play_again[0] == 'e':
        play = False
        break
    elif play_again[0] == 'p':
        while tries > 0:
            print("\n" + "".join(current))
            if "-" not in current:
                print("You guessed the word!\nYou survived!")
                break
            choice = input("Input a letter: ")
            if len(choice) != 1:
                print("You should input a single letter")
                continue
            if choice not in ascii:
                print("Please enter an English letter")
                continue
            if choice.lower() in guesses:
                print("You've already guessed this letter")
                continue
            if choice.lower() in answer_set:
                answer_set.discard(choice)
                for i in range(len(answer)):
                    if choice.lower() == answer[i]:
                        current[i] = answer[i]
                        guesses.append(choice.lower())
            else:
                if choice not in current:
                    print("That letter doesn't appear in the word")
                    guesses.append(choice.lower())
                else:
                    print("No improvements")
                tries -= 1
                print(f"You have {tries} tries remaining")
        else:
            print("You lost!")

    else:
        continue