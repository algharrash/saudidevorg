#datetime module in python

import datetime as dt

x = dt.datetime.now()

print("Current year is: ", x.year)
print("Current day number in the year is: ", x.strftime("%j"))
