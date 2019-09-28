# python lambda part 2

def myfunc(n):
    return lambda a , b: n * (a + b)

result = myfunc(10)
print(result(2,3))

