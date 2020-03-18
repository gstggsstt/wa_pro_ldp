from gen.gen import generator
from privKV.algo import *
import numpy as np
import pdb

if __name__ == '__main__':
    N = 1000000
    k = 5
    e = 0.2
    data = generator(N, k).gen()

    fk = np.zeros([k])
    vk = np.zeros([k])
    for s in data:
        for j in range(k):
            if j in s:
                fk[j] += 1
                vk[j] += s[j]

    fk /= N
    mk = vk/(N*fk)
    print(fk, mk)
    good_fk = fk
    good_mk = mk

    c = Collector(data, k)
    fk, mk = PrivKVM2(c, e, 0.02, good_mk)
    print(fk, mk)

    print('RE:')
    print(np.median(np.abs(fk-good_fk)/good_fk))
    print('Log(MSE):')
    print(np.log(np.mean((mk-good_mk)**2)))
    print('Error mk:')
    print(mk-good_mk)
