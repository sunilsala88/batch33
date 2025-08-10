
#rev a string

str1='reliance'

l1=[4,5,67,7]
l1.reverse()
print(l1)

new=""
l2=[-1,-2,-3,-4,-5]
print(list(range(-1,-(len(str1)+1),-1)))

for i in range(-1 , -(len(str1)+1) , -1):
    new=new+str1[i]
print(new)

new=""
for i in str1:
    new=i+new
print(new)


print(list(range(6,-1,-1)))
new=""
for i in range(len(str1)-1 ,-1,-1):
    new=new+str1[i]
print(new)


new=""
i=-1
while True:
    if i==-(len(str1)+1):
        break
    new=new+str1[i]
    i=i-1
print(new)

new=""
i=0
while True:
    if i==len(str1):
        break
    new=str1[i]+new
    i=i+1
print(new)

new=""
i=len(str1)
while True:
    if i==0:
        break
    i=i-1
    new=new+str1[i]
print(new)