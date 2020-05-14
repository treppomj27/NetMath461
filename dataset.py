
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Dataset:
    def __init__(self, data, name='X'):
        # Reformat the dataset
        self.name = name
        self.values = np.array(data).reshape((-1, 1))
        del name, data
        self.N, self.M = self.values.shape

        # Check to ensure the dataset is properly formatted
        if self.M != 1:
            raise ValueError('ValueError: Dataset is not one-dimensional.')
        elif not self.N >= 1:
            raise ValueError('ValueError: Dataset has no values.')

        # Compute the distinct values within the dataset
        Distinct_Values = []
        for i in range(0, self.N):
            distinct = True
            for j in range(0, i):
                if self.values[i][0] == self.values[j][0]:
                    distinct = False
            if distinct:
                Distinct_Values.append(self.values[i][0])
        Distinct_Values.sort()
        self.distinct_values = np.array(Distinct_Values).reshape((-1, 1))
        del Distinct_Values
        self.D = self.distinct_values.shape[0]

        # Compute the relative frequency for each distinct value
        Relative_Frequencies = []
        for i in range(0, self.D):
            ctr = 0
            for j in range(0, self.N):
                if self.distinct_values[i] == self.values[j]:
                    ctr += 1
            Relative_Frequencies.append(ctr / self.N)
        self.relative_frequencies = np.array(Relative_Frequencies).reshape((-1, 1))
        del Relative_Frequencies

        # Compute the expected value
        Expectation = 0
        for i in range(0, self.D):
            Expectation += self.distinct_values[i] * self.relative_frequencies[i]
        self.expect = Expectation
        del Expectation

        # Compute the variance
        Variance = 0
        for i in range(0, self.D):
            Variance += (self.distinct_values[i] - self.expect)**2 * self.relative_frequencies[i]
        if Variance < 0:
            raise ValueError('ValueError: Variance can\'t be negative.')
        self.var = Variance
        del Variance
        self.standdev = np.sqrt(self.var)

    def print_v(self, sort=True):
        """
        Prints the dataset's values.

        :param sort: (bool) Whether the values will be sorted
        :return: (void)
        """
        print('Values of ' + self.name + ':')
        if sort:
            print(np.sort(self.values[:, 0]), '\n')
        else:
            print(self.values[:, 0], '\n')

    def print_dv(self):
        """
        Prints the dataset's distinct values.

        :return: (void)
        """
        print('Distinct Values of ' + self.name + ':')
        print(self.distinct_values[:, 0], '\n')

    def print_rf(self):
        labels = ['Distinct Value', 'Relative Frequency']
        report = pd.DataFrame(np.hstack((self.distinct_values, self.relative_frequencies)), columns=labels)
        if self.values.dtype == 'int64':
            report['Distinct Value'] = report['Distinct Value'].astype(int)
        print(' Dataset ' + self.name + ':')
        print(report.to_string(index=False), '\n')

    def print_evs(self):
        labels = ['Expectation', 'Variance', 'Standard Deviation']
        evs = np.array([self.expect, self.var, self.standdev]).reshape((1, -1))
        report = pd.DataFrame(evs, columns=labels)
        print(' Dataset ' + self.name + ':')
        print(report.to_string(index=False), '\n')

    def plot_rf(self):
        plt.figure()
        plt.bar(self.distinct_values[:, 0], self.relative_frequencies[:, 0], width=0.1, color='purple')
        plt.scatter(self.distinct_values, self.relative_frequencies, color='orange')
        plt.axvline(x=self.expect, ymin=0, ymax=1, color='green')
        plt.xlim(min(self.distinct_values) - 0.5, max(self.distinct_values) + 0.5)
        plt.ylim(0, min(1, np.max(self.relative_frequencies) * 1.25))
        plt.xlabel('x')
        plt.ylabel('Relative Frequency')
        plt.title('Relative Frequency Plot of ' + self.name)
        plt.legend(['Expectation = ' + str(float(np.round(self.expect, 3))), 'Relative Frequencies'])

    def plot_cdf(self):
        plt.figure()
        plt.axvline(x=self.expect, ymin=0, ymax=1, color='green')
        old_height, height = 0, 0
        x1, x2 = min(self.distinct_values) - 0.5, self.distinct_values[0][0]
        y1 = height
        x3 = self.distinct_values[0][0]
        old_height = height
        height += self.relative_frequencies[0][0]
        y3, y4 = old_height, height
        plt.plot([x1, x2], [y1, y1], 'b-')
        plt.plot([x3, x3], [y3, y4], 'b-')
        for i in range(1, self.D):
            x1, x2 = self.distinct_values[i-1][0], self.distinct_values[i][0]
            y1 = height
            x3 = self.distinct_values[i][0]
            old_height = height
            height += self.relative_frequencies[i][0]
            y3, y4 = old_height, height
            plt.plot([x1, x2], [y1, y1], 'b-')
            plt.plot([x3, x3], [y3, y4], 'b-')
        plt.plot([self.distinct_values[self.D-1][0], self.distinct_values[self.D-1][0] + 0.5], [height, height], 'b-')
        plt.xlabel('x')
        plt.ylabel('F(x)')
        plt.title('Cumulative Distribution Function of ' + self.name)
        plt.legend(['Expectation = ' + str(float(np.round(self.expect, 3))), 'F(x)'])


def cumdist(a, X):
    CD = 0
    i = 0
    while i < X.D and X.distinct_values[i][0] <= a:
        CD += X.relative_frequencies[i][0]
        i += 1
    return np.round(CD, 6)


def prob(A, X):
    P = 0
    for i in range(0, A.D):
        for j in range(0, X.D):
            if A.distinct_values[i] == X.distinct_values[j]:
                P += X.relative_frequencies[j]
    return float(P)
