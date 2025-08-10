

# stock_prices={'tsla':500,'goog':700,'reliance':678,'nifty':456,'nvda':980}

# for i,j in stock_prices.items():
#     print(i,":",j)

# portfolio=[]

# while True:
#     name=input('enter the stock to buy (q to quit)')
#     print(name)
#     if name.lower()=='q':
#         break
#     if name=='nvda':
#         print('you cannot trade this stock try something else')
#         continue

#     found=stock_prices.get(name)
#     if found:
#         portfolio.append(name)
#     else:
#         print('this stock does not exist type again')

# print(portfolio)

#generate a list of all num from 1 to 100 but no num div by 5

# i=0
# l1=[]
# while True:
#     if i==100:
#         break

#     print(i)
#     i =i+1
#     if i%5==0:
#         continue
#     l1.append(i)


# print(l1)

capital=1000
interest=0.08
current_capital=capital
year=0
while True:
    if current_capital>2*capital:
        break
    current_capital=current_capital+(current_capital*interest)
    year=year+1

print(year)
