#Day 12 challenge

x = 5
y = 7
txt = "Please, I want {} sandwishes and {} donutes"

txt = txt.replace("I", "we")
txt = txt.replace("a", "A")
txt = txt.format(x, y)

print(txt)

