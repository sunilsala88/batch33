

#in a txt file you can only store strings

data='amzn is bad'

# f1=open('data.txt','w')
# f1.write(data)
# f1.close()


# f2=open('data.txt','r')
# d=f2.read()
# print(d)
# f2.close()


f3=open('data.txt','a')
f3.write('\nthis is new line')
f3.close()