class student:
    college="university of engineering and techonology"
    
    def __init__(self,name,marks):
        print("adding new student...")
        self.name=name
        self.marks=marks
    #used static method to remove self parameter
    @staticmethod
    def hi():
        print("using @decorator to make static method")

    def hello(self):
        print("welcome student",self.name)
    def get_marks(self):
        return self.marks

s1=student("maaz",[20,23,26])
s1.hello()
s1.hi()
print(s1.get_marks())
