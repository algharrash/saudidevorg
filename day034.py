#Python functions part 2

def count_to_zero(x):
    if x == 0:
        print(0)
    else:
        print(x)
        count_to_zero(x-1)
print("recusrsive method to count to 0:")
count_to_zero(10)

def the_big_number(*k):
    result = 0
    for x in k:
        if x > result: result = x
    return result

print("The bigger number is:")
print(the_big_number(20, 150, 14, 30, 250))