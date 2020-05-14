
import numpy as np
import matplotlib.pyplot as plt


def distinct(_x):
    _d = []
    for i in range(0, _x.shape[0]):
        add = True
        for j in range(0, i):
            if _x[i] == _x[j]:
                add = False
        if add:
            _d.append(_x[i])
    return np.sort(np.array(_d))


def frequency(_x):
    _d = distinct(_x)
    _f = []
    for i in range(0, _d.shape[0]):
        occ = 0
        for j in range(0, _x.shape[0]):
            if _d[i] == _x[j]:
                occ += 1
        _f.append(occ)
    return np.array(_f)


def relative_frequency(_x):
    _d = distinct(_x)
    _rf = []
    for i in range(0, _d.shape[0]):
        ctr = 0
        for j in range(0, _x.shape[0]):
            if _d[i] == _x[j]:
                ctr += 1
        _rf.append(ctr)
    _rf = np.array(_rf)
    return _rf/np.sum(_rf)


def expectation(_x):
    _d = distinct(_x)
    _rf = relative_frequency(_x)
    _e = 0
    for i in range(0, _d.shape[0]):
        _e += _d[i] * _rf[i]
    return _e

def variance(_x):
    _d = distinct(_x)
    _rf = relative_frequency(_x)
    _e = expectation(_x)
    _var = 0
    for i in range(0, _d.shape[0]):
        _var += (_d[i] - _e)**2 * _rf[i]
    return _var


# low = 1
# high = 10
# X = np.random.randint(low, high + 1, 100)
X = np.array([1, 1, 1, 3, 4])

D = distinct(X)
F = frequency(X)
RF = relative_frequency(X)
E = expectation(X)
VAR = variance(X)

print('Dataset =\n', X, '\n')
print('Expectation =', round(E, 3))
print('Variance = ', round(VAR, 3))

plt.subplot(2, 1, 1)
plt.bar(D, RF, width=0.1, color='purple')
plt.scatter(D, RF, color='orange')
plt.scatter(D, np.zeros(D.shape), color='blue')
plt.axvline(x=E, ymin=0, ymax=1, color='green')
plt.xlim(min(D) - 0.5, max(D) + 0.5)
plt.ylim(0, min(1, np.max(RF)*1.2))
plt.xlabel('x')
plt.ylabel('Relative Frequency')
plt.title('Relative Frequency Plot of X')
plt.legend(['Expectation = ' + str(round(E, 3)), 'Relative Frequencies'])

plt.subplot(2, 1, 2)
plt.axvline(x=E, ymin=0, ymax=1, color='green')
N = D.shape[0] - 1
height = 0
plt.plot([0, D[0]], [height, height], 'b-')
for ctr in range(0, N):
    height_old = height
    height += RF[ctr]
    plt.plot([D[ctr], D[ctr]], [height_old, height], 'b-')
    plt.plot([D[ctr], D[ctr+1]], [height, height], 'b-')
plt.plot([D[N], D[N]], [height, 1], 'b-')
plt.plot([D[N], D[N] + 0.5], [1, 1], 'b-')
plt.xlim(min(D) - 0.5, max(D) + 0.5)
plt.ylim(0, 1.1)
plt.xlabel('x')
plt.ylabel('F(x)')
plt.title('Cumulative Distribution Function of X')
plt.legend(['Expectation = ' + str(round(E, 3)), 'F(x)'])

plt.show()
