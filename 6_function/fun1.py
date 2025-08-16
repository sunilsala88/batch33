print('hello')





#function defination
def average(prices):
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