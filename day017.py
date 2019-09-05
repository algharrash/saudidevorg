#Python Tuplues Part 2

welist = ['Ali', 'Khadija']
us = tuple(welist)
kids = tuple(('Ahmad', 'Fatimah'))
our_family = us + kids

print("Our Family members are:")
print(our_family)

print("Check if Ahmad a member of the family:")

if 'Ahmad' in our_family:
    print("Yes, Ahmad is a member of the family")

print("The total of the family members are:")
print(len(our_family))

print("Fatimah order in the family is number:")
print(our_family.index("Fatimah"))

