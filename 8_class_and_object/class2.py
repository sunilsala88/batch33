


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
        pass

    def sell_stock(self,stock_name):
        pass

u1=Broker('matt',568,1000)
u2=Broker('rock',569,2000)
print(u2)

