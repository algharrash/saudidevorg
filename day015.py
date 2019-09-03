#Python list part 3

mylist = list(('A', 'B', 'C', 'D', 'E', 'F'))

print(mylist)

#add item to the end of the list
mylist.append('H')
print("Print mylist after appending an item")
print(mylist)

#print how many items in the list
print("Number of items in mylist:")
print(len(mylist))

#insert an item in specific place in the list
mylist.insert(6, "G")
print("print the list after inserting an item in position 6")
print(mylist)

#removing an item from a list
mylist.remove('H')
mylist.pop(6)
print("print mylist after removing item H & G")
print(mylist)

#copy mylist and then clear it
otherlist = mylist.copy()
mylist.clear()
print("printing my list after clearing it")
print(mylist)
print("printing otherlist")
print(otherlist)

#reverse the order of otherlist
otherlist.reverse()
print("print otherlist after reversing it")
print (otherlist)





