import numpy as np
import pandas as pd
import scipy.stats as stats


class PCAAlgorithm:
    @staticmethod
    def train(input):
        input = pd.DataFrame(input)
        correlation_matrix = input.corr()
        eigenvalues, eigenvectors = np.linalg.eig(correlation_matrix)
        biggest_eigenvalue_index = np.argmax(eigenvalues)
        biggest_eigenvector = eigenvectors[biggest_eigenvalue_index]
        output_vector = []
        for row in input:
            y_value = np.dot(biggest_eigenvector, row)
            output_vector.append(y_value)
        return output_vector

