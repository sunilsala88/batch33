

import datetime
dt1=datetime.datetime.now()
print(dt1)
import datetime as dt
dt2=dt.datetime.now()
print(dt2)

start=dt.datetime(2025,8,1)
print(start)

u1=dt.timedelta(days=1)
print(u1)

i=0
while True:
    if i==30:
        break
    i=i+1

    b=start.weekday()
    if b==0:
        print(start)
    # print(start)
    start=start+u1