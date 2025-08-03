

l1=[22,33,44,55,99,88,77]
high=l1[0]
for i in l1:
    if high<i:
        high=i

print(high)

pnl= [+10, -20, +15, +30, -5]
count=0
for i in pnl:
    if i>0:
        count=count+1

print(count)

prices=[100, 120, 130, 140, 150]
total=0
for i in prices:
    total=total+i
avg=total/len(prices)
print(avg)

count=0
for i in prices:
    if i>avg:
        count=count+1
print(count)

#vwap
p=[100, 105, 110]
v=[200, 150, 300]
sum_of_volume=0
sum_of_pv=0
for i in range(len(p)):
    sum_of_volume=sum_of_volume+v[i]
    sum_of_pv=sum_of_pv+(p[i]*v[i])
vwap=sum_of_pv/sum_of_volume
print(vwap)