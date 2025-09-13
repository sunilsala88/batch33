

# import datetime
import datetime as dt

dt1=dt.datetime(2023, 1, 1, 12, 0, 0)
print(dt1)

d1=dt.date(2023, 1, 1)
print(d1)

t1=dt.time(12, 0, 0)
print(t1)

d1=dt.timedelta(days=1)
print(d1)

print(dt1+d1)

n1=dt.datetime.now()
print(n1)