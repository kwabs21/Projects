import random

EASY_LEVEL = 10
HARD_LEVEL = 5

def check(guess, answer,turns):
    """ checks answer against guess. Returns turns left"""
    if guess > answer:
        print("Too High ")
        return  turns -1
    elif guess < answer:
        print("Too low ")
        return turns -1
    else:
        print("You win")

def difficulty():
    level = input("Choose 'easy' or 'hard'. ")
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL
def game():
    answer = random.choice(range(0,101))
    turns = difficulty()


    guess = 0
    while guess != answer:
        print(f"You have {turns} remaining to guess the number.")
        guess = int(input("Choose a whole number between '1' and '100'"))
        turns = check(guess,answer,turns)
        if turns == 0:
            print("You have run out of guesses. You lose")
            return
        elif guess != answer:
            print("Guess again")

game()