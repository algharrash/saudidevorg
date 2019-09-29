#Day 039 & 040 challenge code

def num_power(x,y):
    if y == 0:
        return 1
    else:
        return x * num_power(x, y-1)

print("The result of 5^3 is: ", num_power(5,3))

myList = [-4, -6, -5, -1, 2, 3, 7, 9, 88]

b = lambda a : a > 0

print("The postive numbers in myList:")
for x in myList:
    if(b(x)) : print(x)

