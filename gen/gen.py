import random
import numpy as np

class generator:
    ''' PrimKV Data generator '''

    def __init__(self, n, k, sd=-1):
        self.n = n
        self.k = k
        tempstate = random.getstate()
        if sd != -1:
            self.sd = sd
            random.seed(sd)
        self.state = random.getstate()
        random.setstate(tempstate)

    def gen(self):
        ''' returns a list of maps '''
        tempstate = random.getstate()
        random.setstate(self.state)
        fk=[random.random()/2+0.5 for i in range(self.k)]
        mk=[random.random()*2-1 for i in range(self.k)]
        x = [
                {i:min(max(np.random.normal(mk[i]),-1),1) for i in range(self.k) if random.random() < fk[i]}
                #{i:random.random()*2-1 for i in range(self.k) if random.random() < fk[i]}
                for j in range(self.n)
            ]

        self.state = random.getstate()
        random.setstate(tempstate)
        return x
