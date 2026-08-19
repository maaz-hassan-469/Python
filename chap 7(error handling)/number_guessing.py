import random
secret=random.randint(1,50)
guesses=0

print("Welcome to the number guessing game!")

while True:
    try:
        guess=int(input("guess the number between 1 to 50: "))
    except ValueError:
        print("you enetered the wrong inout please try again!")
        continue

    guesses=guesses+1
    if  guess>secret:
     print("you entered high number!")
    elif guess<secret:
     print("You entered low number!")
    else:
     print(f"Correct!you guessed the right number in {guesses} tries")
     break



