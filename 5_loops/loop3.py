#type 4
data={"ticker": "TSLA", "quantity": 5000, "average_buy_price": 600}
print(list(data.keys()))
print(list(data.values()))
print(list(data.items()))

for i in data:
    print(i,data[i])

#type 4
for i,j in data.items():
    print(i,j)

stock_prices={'tsla':500,'nvda':400,'amzn':890}
sum1=0
for i,j in stock_prices.items():
    sum1=sum1+j

print(sum1)
large=0
large_key=0
for i,j in stock_prices.items():
    if j>large:
        large=j
        large_key=i

print(large_key,large)