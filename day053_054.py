#week 8 challenge

import module_day53_54 as md 
import datetime as dt 

print("8 + 1 = ", md.add(8, 1))
print("2 - 4 = ", md.subtract(2, 4))
print("6 * 6 = ", md.multiply(6, 6))
print("2 / 8 = ", md.divide(2, 8))

currentDate = dt.datetime.now()

print("Current Year: ", currentDate.year)
print("Today date and time: ", currentDate)
print("Current Month: ", currentDate.month)
print("Current Day: ", currentDate.day)

yesterDay = dt.datetime.now() - dt.timedelta(days=1)
nextDay = dt.datetime.now() + dt.timedelta(days=1)

print("Ysterday: ", yesterDay)
print("Tomorrow: ", nextDay)

