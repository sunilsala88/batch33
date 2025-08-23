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

    def __init__(self,name,email,roll_no,g):
        self.name=name
        self.email=email
        self.roll_no=roll_no
        self.gender=g
    
    def intro(self):
        return 'my name is '+self.name

s1=Student(name='sam',email='sam@gmail.com',roll_no=50,g='m')
s2=Student(name='ravi',email='ravi@gmail.com',roll_no=66,g='m')

print(s1.school_name)
print(s2.school_name)

print(s1.intro())
print(s2.intro())


class Book:

    def __init__(self,title, author, price, quantity):
        self.title=title
        self.author=author
        self.price=price
        self.quantity=quantity
    
    def get_price(self):
        return self.price
    
    def set_price(self,new_price):
        self.price=new_price

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, new_quantity):
        self.quantity=new_quantity
    
    def sell(self, number_sold):
        self.quantity=self.quantity-number_sold

    def restock(self, number_added):
        self.quantity=self.quantity+number_added
    

b1= Book(title="1984", author="George Orwell", price=29.99, quantity=100)

print(b1.get_price())
b1.set_price(35)
print(b1.get_price())
b1.sell(40)
print(b1.get_quantity())


class Circle:
    Pi=3.14

    def __init__(self,radius):
        self.radius=radius
    
    def __repr__(self):
        return 'Circle with radius '+str(self.radius)

    def area(self):
        return self.Pi*(self.radius**2)

    def circumference(self):
        return 2*self.Pi*self.radius
    
c1=Circle(10)
print(c1.radius)
print(c1.area())
print(c1.circumference())

c2=Circle(15)
print(c2.radius)
print(c2.area())
print(c2.circumference())

print(c1)
print(c2)

#what is self