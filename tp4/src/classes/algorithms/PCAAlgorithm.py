import numpy as np
import pandas as pd
import scipy.stats as stats


class PCAAlgorithm:
    @staticmethod
    def train(input):

        input = pd.DataFrame(input)
        correlation_matrix = input.corr()

        correlation_matrix = np.array(correlation_matrix)
        input = np.array(input)

        eigenvalues, eigenvectors = np.linalg.eig(correlation_matrix)
        pc1 = []
        pc2 = []
        for row in input:
            y_value1 = np.dot(eigenvectors.T[0], row)
            y_value2 = np.dot(eigenvectors.T[1], row)
            pc1.append(y_value1)
            pc2.append(y_value2)
        return pc1, pc2

