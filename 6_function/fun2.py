


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