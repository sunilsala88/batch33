


def add(num1 :str ,num2 :str)-> str:
    """
    this function will add 2 num
    """
    ans=num1+num2
    return ans

a=add('10','2')
print(a)


def factorial(num:int)->list:

    fact=num
    while True:
        num=num-1
        if num==0:
            break

        fact=fact*num
    return fact

n=factorial(5)
print(n)

def maximum(numbers_list:list)->int:
    """
    this func returns the highest num in the list
    """
    high=numbers_list[0]
    for i in numbers_list:
        if high<i:
            high=i
    
    return high

h=maximum([55,66,99,77])
print(h)

def area(radius:int)->int:
    """
    this func return the area of circle taking radius as input
    """
    return 3.14*(radius**2)

a=area(10)
print(a)


def merge(list1:list,list2:list)->list:

    for i in list2:
        list1.append(i)
    return list1

l=merge([22,33,44],[66,77,88])
print(l)


def hour_to_sec(hours:int)->int:
    return hours*60*60

s=hour_to_sec(2)
print(s)