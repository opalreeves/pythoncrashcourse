class LCG:
    def __init__(self, seed):
        self.seed = seed
        self.modulus = 2**31 - 1
        self.multiplier = 48271
        self.increment = 0

    def random(self):
        self.seed = self.seed * self.multiplier
        self.seed = self.seed + self.increment
        self.seed = self.seed % self.modulus
        return self.seed / self.modulus
    
lcg = LCG(4722048403846384983726154843)

for i in range(10):
    print(math.floor(lcg.random()*10))
