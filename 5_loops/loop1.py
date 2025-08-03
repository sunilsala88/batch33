

l1=[44,55,66,77,88]

#iterate/looping
total=0

for p in l1:
    total=total+p

print(total)
n=len(l1)
print(n)
print('average',total/n)

#type 1
for i in l1:
    print(i)

#type 2
a=list(range(100))
print(a)
for i in range(10):
    print('hello world')

#type 3 
l2=[5,6,78,89,33,85,78,67]
for i in range(len(l2)):
    print(l2[i])

#square all the elem of the list
list3=[2,3,4,5]
new_list=[]
for i in list3:
    new_list.append(i**2)
print(new_list)