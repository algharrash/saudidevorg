#Day 018 and 019 Challenge

#First part of the challange
prog_langs = ['java', 'python', 'swift']
print("print list prg_langs:")
print(prog_langs)

prog_langs.append("php")
print("print list prg_langs after appending a new item:")
print(prog_langs)

print("print how many php occured in prog_langs list:")
print(prog_langs.count('php'))

print("the position of swift in prog_langs list:")
print(prog_langs.index('swift'))

print("print prog_langs after removing php item:")
prog_langs.remove('php')
print(prog_langs)

#second part of the challenge
mylangs = tuple(prog_langs)

if 'python' in mylangs:
    print('The item python is in the tuple mylangs')