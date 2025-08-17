


# #fun defination
# def factorial(num:int)->int:
#     """
#     this function takes a number and calculates the factorial
#     """

#     fact=num
#     i=num
#     while True:
#         if i==1:
#             break

#         i=i-1
#         fact=fact*i
#     return fact

# ans=factorial(5)
# print(ans)

# def print_num(num1:int,num2:int=1):
#     print('num1 is ',num1)
#     print('num2 is ',num2)

# #pos argument
# print_num(10)

# #keyword argument
# print_num(num2=30,num1=33)

# #local and global variable




def factorial(num:int)->int:
    """
    this function takes a number and calculates the factorial
    """
    global number
    print(a)
    number=30
    fact=num
    i=num
    while True:
        if i==1:
            break

        i=i-1
        fact=fact*i
    return fact

number=5
a=10
ans=factorial(number)

print(ans)
print(number)


#global var can be accesed inside a function
#any var that you create inside a function is called local variable