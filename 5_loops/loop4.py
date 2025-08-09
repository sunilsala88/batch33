

#type1
list1=[44,55,66,77,88]
for i in list1:
    print(i)

#type2

for i in range(10):
    print('hello')

#type3

for i in range(len(list1)):
    print(list1[i])

#type 4
stock_prices={'tlsa':500,'goog':900,'amzn':567}
for i,j in stock_prices.items():
    print(i,j)

num=100
total=0
for i in range(num+1):
    total=total+i

print(total)

print(list(range(1,101)))
total=0
for i in range(1,num+1):
    total=total+i
print(total)

#1 1 2 3 5 8 13 21 34 55 ...

fib=[1,1]
num1=fib[0]
num2=fib[1]

for i in range(8):
    num3=num1+num2
    fib.append(num3)
    num1=num2
    num2=num3
    
print(fib)