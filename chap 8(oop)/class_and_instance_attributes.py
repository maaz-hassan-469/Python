class student:
    #class attributes
    college_name="punjab college"
    name="hassan"#it will not print
    def __init__(self,name,age,marks):
        #object attributes
        self.name=name #precedence of object attribute is greater than class attribute
        self.age=age 
        self.marks=marks
        print("adding new student...")

s1=student("maaz",20,[20,30,40])
print(s1.name,s1.age,s1.marks)

    
    

