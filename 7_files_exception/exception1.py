

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