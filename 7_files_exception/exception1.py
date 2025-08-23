

# try:
#     num1=10
#     num2=0
#     ans=num1/num2
#     print(ans)
# except:
#     print('something went wrong')


try:
    num1=10
    num2='2'
    ans=num1/num2
    print(ans)
except Exception as e:
    print(e)
    print('something went wrong')

print('this is last line')

# list1=[44,55,66,77,88]
# try:
#     i=int(input('enter the index number'))
#     v=list1[i]
#     print(v)
# except:
#     print('invalid index')

try:
    f1=open(r'/Users/algo trading 2025/batch33/7_files_exception/data.txt','r')
    d=f1.read()
    print(d)
except:
    print('file not found')