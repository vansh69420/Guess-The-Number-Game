import random
from art import logo


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
chosed_number = random.randint(1,100)
# print(chosed_number)

def in_easy():
    guess_times = 10
    loop = True
    while loop:
        print(f"You have {guess_times} attempts remaining to guess the number.")
        user_guess = int(input("Make a Guess : "))
        guess_times -= 1
        if guess_times == 0:
            print("You run out of guesses , You lose")
            loop = False
        elif user_guess == chosed_number:
            print("You win, you guessed it right")
            loop = False
        elif user_guess > chosed_number:
            print("Too High")
        elif user_guess < chosed_number:
            print("Too Low")
        
        




    

def in_hard():
    guess_times = 5
    loop = True
    while loop:
        print(f"You have {guess_times} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        guess_times -= 1
        if guess_times == 0:
            print("You run out of guesses , You lose")
            loop = False
        elif user_guess == chosed_number:
            print("You win, you guessed it right")
            loop = False
        elif user_guess > chosed_number:
            print("Too High")
        elif user_guess < chosed_number:
            print("Too Low")



def in_normal():
    guess_times = 7
    loop = True
    while loop:
        print(f"You have {guess_times} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        guess_times -= 1
        if guess_times == 0:
            print("You run out of guesses , You lose")
            loop = False
        elif user_guess == chosed_number:
            print("You win, you guessed it right")
            loop = False
        elif user_guess > chosed_number:
            print("Too High")
        elif user_guess < chosed_number:
            print("Too Low")

difficulty = input("Choose a difficulty, Type 'easy' or 'normal' or 'hard' : ")

if difficulty == "easy":
    in_easy()
elif difficulty == "hard":
    in_hard()
elif difficulty == "normal":
    in_normal()
else:
    print("You enter the invalid difficulty")
