import numpy as np
from math import exp
from . import utils
from random import random, randint
import matplotlib.pyplot as plt


class Collector:
    def __init__(self, data, d):
        self.data = data
        self.d = d

    def get(self, m, e1, e2):
        return [LPP(s, self.d, e1, e2, m) for s in self.data]


def VPP(v, e):
    ''' discretization and perturbation, returns v* '''
    v = discretization(v)
    v = perturbation(v, e)
    return v


def discretization(v):
    v = 1 if random() < (1.0+v)/2 else -1
    return v


def perturbation(v, e):
    p = exp(e)/(1+exp(e))
    v = v if random() < p else -v
    return v


def LPP(Si, d, e1, e2, m_=None):
    ''' returns: (j, kj, v*) '''
    j = randint(0, d-1)
    p = exp(e1)/(1+exp(e1))
    if j in Si:
        vstar = VPP(Si[j], e2)
        kj, v = (1, vstar) if random() < p else (0, 0)
        return {'j': j, 'kj': kj, 'v': v}
    else:
        if m_ is None:
            vstar = VPP(random()*2-1, e2)
        else:
            vstar = VPP(m_[j], e2)
            # vstar = discretization(m_[j])
        kj, v = (0, 0) if random() < p else (1, vstar)
        return {'j': j, 'kj': kj, 'v': v}


def PrivKV(c, e1, e2, m=None):
    ''' basic privKV '''
    sample = c.get(m, e1, e2)

    fk, n1_, n2_ = utils.analyze_sample(sample, c.d)
    p1 = exp(e1)/(1+exp(e1))
    if m is None:  # in case of divided by zero
        fk = (fk+p1-1)/(p1*2-1)

    N = n1_+n2_
    p2 = exp(e2)/(1+exp(e2))

    n1 = utils.fix_bound(n1_/(p2*2-1) + (p2-1)/(p2*2-1)*N, N)
    n2 = utils.fix_bound(n2_/(p2*2-1) + (p2-1)/(p2*2-1)*N, N)

    mk = (n1-n2)/N
    return (fk, mk)


def PrivKVM(coll, e, n, good_mk):
    ''' basic privKV '''
    # FIXME: Existing Bugs
    y = []
    fk, mk = PrivKV(coll, e/2, e/2/n)
    for i in range(n-1):
        _, mk = PrivKV(coll, 0, e/2/n, mk)
        print(mk)
        y.append(np.mean(np.abs(mk-good_mk)))
    plt.plot([i for i in range(n-1)], y)
    plt.show()
    return (fk, mk)


def PrivKVM2(c, e, A0, good_mk, t=1.1):
    # FIXME: Existing Bugs
    e1 = e2 = e/t
    m_ = [1] * c.d
    fk, mk = PrivKV(c, e1, e2, m_)
    y = []
    while utils.F(A0, m_, mk) < 0:
        e1 = 0
        e2 = (e2)/t
        m_ = mk
        _, mk = PrivKV(c, e1, e2, mk)
        print(mk)
        y.append(np.mean(np.abs(mk-good_mk)))
    plt.plot([i for i in range(len(y))], y)
    plt.show()
    return (fk, mk)
