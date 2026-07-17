name=input("enter your name: ")
age=int(input("enter your age: "))
char=name[0]
char.lower()
if char=='a' and age>10:
    print("you can watch movie")
else:
    print("you cannot watch movie")