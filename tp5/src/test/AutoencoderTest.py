import numpy as np

from src.classes.functions.ActivationFunctions import TAN_H, TAN_H_DERIVATIVE
from src.classes.functions.LossFunctions import mse_prime, mse
from src.classes.models.NeuralNetwork import NeuralNetwork
from src.classes.layers.DenseLayer import DenseLayer
from src.classes.optimizers.Adam import Adam
from src.classes.utils.TrainingUtils import TrainingUtils
from src.data.fonts import get_characters


# network
net = NeuralNetwork(activation=TAN_H, activation_prime=TAN_H_DERIVATIVE, optimizer = Adam,
                    architecture=[49, 30, 20, 10, 5, 2, 5, 10, 20, 30, 49])

characters = get_characters()

training_set = np.array(TrainingUtils.generate_batches(characters.copy(), 10))
training_expected = training_set.copy()

test_set = np.array(characters.copy())
test_expected = characters.copy()

# train
net.use(mse, mse_prime)
net.fit(training_set, test_set, 1000000000, training_expected, test_expected)

# test
out = net.predict(test_set)[0]
for i in range(len(test_set)):
    print("--------------------------------")
    print("Expected", test_set[i])
    print("--------------------------------")
    print("Result", out[i])
