import datetime as dt
d1=dt.datetime.now()
print(d1)


import pendulum as dt
# time_zone1='America/New_York'
time_zone1='Asia/Kolkata'
d1=dt.now(tz=time_zone1)
print(d1)