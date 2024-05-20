secret_number= 7
guess_count= 0  
while guess_count < 3:
    guess= int(input("guess a number(1-10):"))
    guess_count +=1
    if guess== secret_number:
        print("congratulations, you guessed it!")
        break
    else:
        print("try again")
if guess_count== 3:
    print("sorry you ran out of guesses. the number was", secret_number)
        