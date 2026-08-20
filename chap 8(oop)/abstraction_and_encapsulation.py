#definition of abstraction
"""hiding the implementation details of a class and only showing the essential features to the user"""
#definition of encapsulation
"""wrappigng data and functions into the single unit(object)"""
#4 pillars of object oriented programming
"""
1-Abstraction
2-Encapsultaion
3-Inheritance
4-Polymorphism
"""
#implemntation of abstraction and encapsulation
class Account:
    def __init__(self,bal,acc):
        self.bal=bal
        self.acc=acc

    def debit(self,amount):
        self.bal-=amount
        print("Rs",amount," was debited")
        print("total balance=",self.get_bal())

    def credit( self,amount):
        self.bal+=amount
        print("Rs",amount," was credited")
        print("total balance=",self.get_bal())

    def get_bal(self):
        return self.bal

acc1=Account(30000,12345)
print(acc1.debit(10000))
print(acc1.get_bal())



        

    

