#file handling in python

f = open("myfile.txt", "a")
f.write("This is a test content ^_^")
f.close()

f = open("myfile.txt", "rt")
print(f.read())
f.close()

