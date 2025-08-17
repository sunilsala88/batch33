

#different types of argument/parameter




def add(num1 :str ,num2 :str)-> str:
    """
    this function will add 2 num
    """
    ans=num1+num2
    return ans

#positional argument
a=add('5','6')
print(a)

#keyword argument
a=add(num2='2',num1='10')
print(a)


#default argument

def division(num1:int,num2:int=1)->int:
    a=num1/num2
    return a

d=division(10)
print(d)


def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10,20)