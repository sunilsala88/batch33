print('hello')





#function defination
def average(prices:list)->int:
    """
    this function takes a list and return average of the list
    """
    total=0
    for i in prices:
        total=total+i
    avg=total/len(prices)
    return (avg)

prices=[44,55,66,77]
a=average(prices)
print(a)

customers=[5,6,7,8,9]
b=average(customers)
print(b)


def get_list(num:int)->list:
    """
    this function generates a list of even numbers
    """
    list1=[]
    
    i=0
    while True:
        if len(list1)==num:
            break
        i=i+1
        if i%2==0:
            list1.append(i)
    return list1

l=get_list(10)
print(l)


#get_fib(10)

def get_fib(num:int)->list:
    """
    this func returns a fibonacci numbers
    """

    fib=[1,1]
    num1=fib[0]
    num2=fib[1]

    for i in range(num-2):
        num3=num1+num2
        fib.append(num3)
        num1=num2
        num2=num3
    return fib

f=get_fib(20)
print(f)



def sum_of_num(num1,num2):
    return num1+num2

n=sum_of_num(10,20)
print(n)


def rev_list(l1:list)->list:
    """
    this funct will reverse the given list
    """
    rev=[]

    for i in range(-1, -(len(l1)+1),-1):
        rev.append(l1[i])

    return rev
l2=rev_list([6,7,8,9])
print(l2)

a=[4,5,6,7]
a.reverse()
print(a)