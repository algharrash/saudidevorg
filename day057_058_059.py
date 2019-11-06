#Python  Regular Expressions
import re

myStr = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."

x1 = re.findall('^P+', myStr)
print(x1)

x2 = re.findall('[abc]', myStr)
print(x2)

x3 = re.findall('\S+-\S+', myStr)
print(x3)

x4 = re.split(',', myStr)
print(x4)

x5 = re.sub('Python', '[Python]', myStr)
print(x5)

