

name='sunil'
v=200

def get_intro():
    return 'this is algo trading course'



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