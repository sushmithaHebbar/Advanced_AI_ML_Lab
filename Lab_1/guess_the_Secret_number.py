
from random import randint
attempts=0
max_attempts=5

secret_number=(randint(1,100))

while True:
    try:
        remaining=max_attempts-attempts
        print(f"Total Attempts:{remaining}")
        guess=int(input("Enter your guess: "))
        attempts+=1
        if attempts==max_attempts:
            print(f"Sorry,You have reached the attempts")
            break
        if guess<1 or guess>100:
            print("Please,Enter the numbers bw 1 to 100")
        elif guess<secret_number:
            print("Too low")
        elif guess>secret_number:
            print("Too high")
        else:
            print(f"You have guessed write secret number in {attempts} attempts,Comgratulation")
            print(f"The secret number is {secret_number}")
            print("Thank you for playing")
            break

    except ValueError:
        print("Please,Enter valid number")
        continue
if attempts==max_attempts and guess!=secret_number:
    print("\n Game Over")
    print(f"The secret number was: {secret_number}")
    print("\nThanks for playing!")