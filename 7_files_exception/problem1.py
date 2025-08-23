

stock_prices={'tsla':500,'goog':700,'reliance':678,'nifty':456,'nvda':980}

def print_stocks():
    for i,j in stock_prices.items():
        print(i,":",j)


def buy_stocks():
    porfolio={}

    while True:
        name=input('enter the name of stock (q to quit)')
        if name.lower()=='q':
            break
        found=stock_prices.get(name)
        if found:
            porfolio.update({name:found})
        else:
            print('this stock does not exist try again')
    return porfolio

def save_data(port):
    total=0
    f1=open('data.txt','a')
    for i,j in port.items():
        d1=i+':'+str(j)+'\n'
        f1.write(d1)
        total=total+j

    d2="total"+':'+str(total)+'\n'
    f1.write(d2)
    
    f1.close()

print_stocks()
p=buy_stocks()
save_data(p)

