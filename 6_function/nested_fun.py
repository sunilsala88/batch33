


def fun1(num1,num2):
    print(num1)
    num3=num1*num2
    return num3


def fun2(num5,num6):
    num7=num5+num6
    print(num7)
    return num7


def fun3(num9,num4):
    print(num9**2)
    return (num9-num4)


def main():
    a=fun3(5,3)
    print(a)
    b=fun1(a,2)
    print(b)
    c=fun2(a,b)

main()
#25
#2
#2
#4
#6