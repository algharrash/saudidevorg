#Conditional statments in python

x = 1
y =2
z = 5

#single if statment
if x < y:
    print("x is less than y")

#if with elif & else
if x == y:
    print("x is equal y")
elif x > y:
    print("x is greater than y")
else:
    print("x is less than y")

#one line if else statment
print("x is less than y") if x < y else print("x is greater than y")

#if statment with logical operatoer

if x < y and z > y:
    print("we are done!")
else:
    print("move on")

