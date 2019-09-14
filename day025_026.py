#Day 025 & 026 challenge

#First Challange

myset = {1, 3, 5, 7, 8}

print("Print myset:")
print(myset)

myset.update([4, 8, 12])
print("Print myset after adding 4,8,12 items:")
print(myset)

myset.discard(8)
print("print myset after deleting item (8):")
print(myset)

myset.clear()
print("Print myset after clearing it:")
print(myset)

#Second Challenge

myDictionary = {
    'name' : 'pigeon',
    'type' : 'bird',
    'skin cover' : 'feathers'
}

print("print myDictionary:")
print(myDictionary)

print("the type value in dictionary:")
print(myDictionary['type'])

myDictionary['skin cover'] = ''
print("Print myDictionary after changing (skin cover) item")
print(myDictionary)

