import random
import time
from wordslist import words

hangman_art = {0: (" | ",
                   "   ",
                   "   ",
                   "   "),
               1: (" | ",
                   " o ",
                   "   ",
                   "   "),
               2: (" | ",
                   " o ",
                   " | ",
                   "   "),
               3: (" | ",
                   " o ",
                   "/| ",
                   "   "),
               4: (" | ",
                   " o ",
                   "/|\\",
                   "   "),
               5: (" | ",
                   " o ",
                   "/|\\",
                   "/  "),
               6: (" | ",
                   " o ",
                   "/|\\",
                   "/ \\"),
               7: (" o ",
                   "/|\\",
                   "/ \\")}
def display_hangman(wrong_guess):
    for x in hangman_art[wrong_guess]:
        print(x)
def display_hint(hint):
    print(" ".join(hint))
    print("************************")
def display_answer(answer):
    print(" ".join(answer))
def display_thanks():
    for line in hangman_art[7]:
        print(line)
    print("THANK YOU FOR PLAYING")
def main():
    is_running = True
    answer = random.choice(words).lower()
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guesses = set()
    while is_running:
        counter = 0
        print("""
************************
    HANG MAN GAME
    (BY: YOUSOF)
************************
            """)
        if "_" not in hint:
            display_thanks()
            display_answer(answer)
            break
        elif wrong_guesses == 6:
            display_hangman(wrong_guesses)
            print("the answer was:")
            display_answer(answer)
            break
        display_hangman(wrong_guesses)
        display_hint(hint)
        print("Guesses:")
        for guess in guesses:
            print(guess, end=" ")
        print()
        guess = input("Enter a letter to guess: ").lower()
        if not guess.isalpha():
            print("************************")
            print("invalid guess")
            print("************************")
            time.sleep(1)
            continue
        if guess in guesses:
            print("************************")
            print("already guessed")
            print("************************")
            time.sleep(1)
            continue
        guesses.add(guess)
        if guess == answer:
            print("************************")
            print("CORRECT")
            print("************************")
            print()
            time.sleep(1)
            print("""
************************
     HANG MAN GAME
      (BY: YOUSOF)
************************
                  """)
            display_thanks()
            display_answer(answer)
            is_running = False
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
                    if hint[i] == guess:
                        counter += 1
            if counter >= 1:
                print("************************")
                print("CORRECT")
                print("************************")
                time.sleep(1)
        else:
            print("************************")
            print("WRONG")
            print("************************")
            time.sleep(1)
            wrong_guesses += 1
if __name__ == "__main__":
    main()