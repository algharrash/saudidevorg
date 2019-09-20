#python functions

def count_to_zero(n = 10):
    while n >= 0:
        print(n)
        n -=1

print("call the function with default parameter")
count_to_zero()
print("Call the function with n = 20")
count_to_zero(20)
