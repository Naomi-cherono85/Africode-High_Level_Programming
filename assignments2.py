import random


guess_number=0
secret_number= random.randint(1,100)
attempts= 0
print("Welcome to the number guessing me!")
print("a number between 1 and 100 is chosen, can u guess it?")
while  True:
    guess = int(input("enter your guess: "))
    attempts += 1
    if guess == secret_number:
        print("congratulations! the number you guessed is correct ")

        break
    elif guess < secret_number:
      print("too low, try again!")
    else:
      print("too high, try again")