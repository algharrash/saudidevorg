#Python Iterators

class EvenNum:
    def __iter__(self):
        self.n = 2
        return self
    
    def __next__(self):
        x = self.n 
        self.n += 2
        return x

myNumber = EvenNum()
myitr = iter(myNumber)

n = 10
while (n > 0):
    print(next(myitr))
    n -= 1


