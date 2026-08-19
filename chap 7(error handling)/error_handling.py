num=input("enter a number for table:")
try:
    for i in range(1,11):
        print(f"{int(num)}*{i}={int(num)*i}")
except Exception as e:
    print("invalid input")
except ValueError:
    print("wrong input")



