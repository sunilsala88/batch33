

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


i=1
n=10
total=0
while True:
    if i==n:
        break

    i=i+1
    if i%2==0:
        total=total+i
print(total)

init_bal=50_000
montly=200
interest=0.06
years=20

for i in range(20*12):
    init_bal=init_bal+montly

    # init_bal=init_bal+(init_bal*(interest/12))
    if i%12==0:
        init_bal=init_bal+(init_bal*interest)
print(init_bal)

start=2000
monthly_cont=150
end_result=10_000
interest=0.04
current_inv=start
months=0
while True:
    if current_inv>=end_result:
        break
    months=months+1
    current_inv=current_inv+150
    if months%12==0:
        current_inv=current_inv+(current_inv*interest)
print(months)