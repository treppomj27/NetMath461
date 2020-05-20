
import dataset as ds
from dataset import Dataset
import numpy as np
import matplotlib.pyplot as plt

X = Dataset([1, 2, 3, 4], name='X')
Y = Dataset([4, 5, 6], name='Y')

A = ds.intersect(X, Y, name='A')
B = ds.union(A, X, name='B')

print()
X.print_v()
Y.print_v()
A.print_v()
B.print_v()

# print()
# print('Prob[A, X] =', ds.prob(A, X), '\n')
# print('cumdist[4, X] =', ds.cumdist(4, X), '\n')
#
# X.print_v(sort=True)
# A.print_v(sort=True)
# X.print_dv()
# X.print_rf()
# X.print_evs()
