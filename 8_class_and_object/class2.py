


class Broker:
    broker_name='alpaca'
    stock_prices={'tsla':500,'goog':800,'nvda':678,'jpm':467,'intel':367,'amzn':689}

    def __init__(self,name,id,money):
        self.name=name
        self.id=id
        self.wallet=money
        self.portfolio={}
    
    def __repr__(self):
        return self.name
    
    def get_portfolio(self):
        return self.portfolio
    
    def buy_stock(self,stock_name):
        found=self.stock_prices.get(stock_name)
        if found:
            
            if self.wallet>found:
                self.portfolio.update({stock_name:found})
                self.wallet=self.wallet-found
            else:
                print('you dont have enough money to buy')
        else:
            print('this stock does not exist')

    def sell_stock(self,stock_name):
        found=self.portfolio.get(stock_name)
        if found:
            self.portfolio.pop(stock_name)
            self.wallet=self.wallet-found
        else:
            print('this stock is not in your porfolio')

u1=Broker('matt',568,3000)
u2=Broker('rock',569,2000)
print(u2)

u1.buy_stock('tsla')
print(u1.get_portfolio())
u1.buy_stock('amzn')
print(u1.get_portfolio())
u1.sell_stock('amzn')
print(u1.get_portfolio())
