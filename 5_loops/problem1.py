

stock_prices={'tsla':500,'goog':700,'reliance':678,'nifty':456,'nvda':980}
portfolio=[]

while True:
    name=input('enter the stock to buy (q to quit)')
    print(name)
    if name.lower()=='q':
        break

    found=stock_prices.get(name)
    if found:
        portfolio.append(name)
    else:
        print('this stock does not exist type again')

print(portfolio)
