#class
#blueprint of object

#object
#instance of a class

#attribute

#class attribute
#atrribute common for all object

#object/instance attribute
#different for each object

#method
#any function you create inside a class is called method


#__init__ method is called contructor
#its the first which is executed when you create an object

#pass
#placeholder

#if you want to access instance attribute inside a class 
#then you have to use self


class Student:
    school_name='ambani'
    dress_code='blac_white'

    def __init__(self,name,email,roll_no):
        self.name=name
        self.email=email
        self.roll_no=roll_no
    
    def intro(self):
        return 'my name is '+self.name

s1=Student(name='sam',email='sam@gmail.com',roll_no=50)
s2=Student(name='ravi',email='ravi@gmail.com',roll_no=66)

print(s1.school_name)
print(s2.school_name)

print(s1.intro())
print(s2.intro())