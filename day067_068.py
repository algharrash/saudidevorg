#week 10 challenge

#part one

print("Write the first letter of your name and the last letter")
x = input()
print("The first letter of your name is: ", x[0])
print("The last letter of your name is: ", x[1])

#part two
myStr = "Dear {name}, Your current balance is {balance} $"
print(myStr.format(name="Ahmad Ali", balance = 53.44))
