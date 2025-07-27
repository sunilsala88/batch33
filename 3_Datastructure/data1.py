

l1=['tsla','goog','amzn']
print(l1[0])
print(l1[1:2])
l1.append('nvda')
print(l1)
a=l1.remove('goog')
print(a)
print(l1)
l1.insert(1,'nifty')
print(l1)
a=l1.pop(0)
print(a)
print(l1) 
i=l1.index('nifty')
print(i)