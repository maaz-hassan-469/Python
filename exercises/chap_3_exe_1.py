number=int(input("enter a number to guess it :"))
if number==10:
    print("you guessedd right")
else:
    if number<10:
        print("number is low")
    else:
        print("number is high")