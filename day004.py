import random

#declare different numric variables type
x = 1 #int
y = 1.5 #float
z = -4j #complex

print("Variable x value:")
print(x)
print("type of x variable:")
print(type(x))

print("Variable y value:")
print(y)
print("type of y variable:")
print(type(y))

print("Variable z value:")
print(z)
print("type of z variable:")
print(type(z))

#convert x to float
x1 = float(x)
print("convert x var from int to float:")
print(x1)
print(type(x1))

#convert y to int
y1 = int(y)
print("convert y var from float to int")
print(y1)
print(type(y1))

#convert x to complex
z1 = complex(x)
print("convert x var from int to complex")
print(z1)
print(type(z1))

#generate random number 5 times between 1 to 10
print(random.randrange(1,10))
print(random.randrange(1,10))
print(random.randrange(1,10))
print(random.randrange(1,10))
print(random.randrange(1,10))




