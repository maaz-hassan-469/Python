class student:
    #default constructor
    def __init__(self):
        print("adding new student...")
    name="maaz hassan"
    college="university of engineering and techonology"

class car:
    #parametrized constructor
    def __init__(self,colour,brand):
        print("adding new car...")
        self.colour=colour
        self.brand=brand

s1=student()
print(s1.name)
print(s1.college)
c1=car("blue","BMW")
print(c1.brand)
