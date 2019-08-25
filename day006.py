#casting methods

x = 5
y = 2.5
z = "10"

print("variables and their types before casting")
print(x)
print("the type of x variable")
print(type(x))
print(y)
print("the type of y variable")
print(type(y))
print(z)
print("the type of z variable")
print(type(z))

x = float(x)
y = str(y)
z = int(z)

print("variables and their types after casting")
print(x)
print("the type of x variable after using float method")
print(type(x))
print(y)
print("the type of y variable after using str method")
print(type(y))
print(z)
print("the type of z variable after using int method")
print(type(z))