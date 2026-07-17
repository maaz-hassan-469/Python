import random
number=int(input("enter a number:"))
guess=1
winning_number=random.randint(1,100)
while number!=winning_number:
    if number<winning_number:
        print('too low')
    else:
        print("too high")
    guess+=1
    number=int(input("guess again:"))
    
print(f"you guess right in {guess} attempts")
print(f"the winning number is {winning_number}")