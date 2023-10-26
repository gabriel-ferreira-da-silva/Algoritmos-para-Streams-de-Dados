import sys, math, random
class counter:
    def __init__(self):
        self.count = 0
        self.b = 1

    def update(self):
        p = 1/ math.pow(self.b , (self.count -1))
        e = random.random()
        if e <= p:
            self.count += 1
    
    def getCount(self):
        return math.pow(self.b, self.count)



c = counter()
c.b = 1.5
n = int(sys.argv[1])

for i in range(n):
    r = math.ceil(math.pow(3,i))
    for i in range(r):
        c.update()
    print("# events : ", r)
    print("# counts : ", c.getCount())
    print("-")
    print(" ")