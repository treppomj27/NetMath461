
import dataset as ds
from dataset import Dataset
import numpy as np
import matplotlib.pyplot as plt

# X = Dataset(np.random.randint(low=1, high=(10 + 1), size=(1, 20)))
X = Dataset([1, 1, 2, 3, 3, 3, 4, 5, 5, 8], name='X')
A = Dataset([3, 5, 8], name='A')

print()
print('Prob[A, X] =', ds.prob(A, X), '\n')
print('cumdist[4, X] =', ds.cumdist(4, X), '\n')

X.print_v(sort=True)
A.print_v(sort=True)
X.print_dv()
X.print_rf()
X.print_evs()

X.plot_rf()
X.plot_cdf()

plt.show()
