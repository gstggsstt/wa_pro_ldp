import numpy as np


def analyze_sample(sample, d):
    fk = np.zeros([d])
    n1 = np.zeros([d])
    n2 = np.zeros([d])
    nk = np.zeros([d])
    for s in sample:
        fk[s['j']] += s['kj']
        nk[s['j']] += 1
        if s['v'] == 1:
            n1[s['j']] += 1
        if s['v'] == -1:
            n2[s['j']] += 1
    fk = fk/nk
    return (fk, n1, n2)


def fix_bound(x, N):
    for i in range(len(x)):
        if x[i] > N[i]:
            x[i] = N[i]
        if x[i] < 0:
            x[i] = 0
    return x


def F(A0, m1, m2):
    return A0 - np.mean(np.abs(m1-m2))
