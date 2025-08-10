

# num=1

# while True:
#     if num==11:
#         break
#     print(num)
#     num=num+1

total=0
num=1
while True:
    if num==101:
        break
    print(num)
    total=total+num
    num=num+1

print(total)


fib=[1,1]
num1=fib[0]
num2=fib[1]

i=0

while True:
    if i==8:
        break
    i=i+1
    num3=num1+num2
    fib.append(num3)
    num1=num2
    num2=num3

print(fib)


l2=[44,55,66,77,88]
rev_list=[]
print(list(range(-1,-(len(l2)+1),-1)))
for i in range(-1,-(len(l2)+1),-1):
    rev_list.append(l2[i])
print(rev_list)

print(list(range(-1,-(len(l2)+1),-1)))

rev_list=[]
i=-1
while True:
    if i==-6:
        break
    print(i)
    rev_list.append(l2[i])
    i=i-1
print(rev_list)

#factorial
num=5
fact=num
for i in range(1,num):
    print(i)
    fact=fact*i
print(fact)

i=num
fact2=num
while True:
    i=i-1
    if i==0:
        break
    fact2=fact2*i
    print(i)

print(fact2)