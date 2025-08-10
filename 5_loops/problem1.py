

stock_prices={'tsla':500,'goog':700,'reliance':678,'nifty':456,'nvda':980}

for i,j in stock_prices.items():
    print(i,":",j)

portfolio=[]

while True:
    name=input('enter the stock to buy (q to quit)')
    print(name)
    if name.lower()=='q':
        break
    if name=='nvda':
        print('you cannot trade this stock try something else')
        continue

    found=stock_prices.get(name)
    if found:
        portfolio.append(name)
    else:
        print('this stock does not exist type again')

print(portfolio)

#generate a list of all num from 1 to 100 but no num div by 5