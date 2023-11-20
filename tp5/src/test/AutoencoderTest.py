import numpy as np

from src.classes.ActivationFunctions import TAN_H, TAN_H_DERIVATIVE
from src.classes.LossFunctions import mse_prime, mse
from src.classes.NeuralNetwork import NeuralNetwork
from src.classes.layer.Layer import Layer
from src.classes.optimizers.Adam import Adam
from src.classes.utils.TrainingUtils import TrainingUtils
from src.data.fonts import get_characters

# network
net = NeuralNetwork(activation=TAN_H, activation_prime=TAN_H_DERIVATIVE, optimizer = Adam)
net.add(Layer(input_size=49, output_size=30, optimizer=Adam()))
net.add(Layer(input_size=30, output_size=20, optimizer=Adam()))
net.add(Layer(input_size=20, output_size=10,optimizer=Adam()))
net.add(Layer(input_size=10, output_size=5, optimizer=Adam()))
net.add(Layer(input_size=5, output_size=2, optimizer=Adam()))
net.add(Layer(input_size=2, output_size=5, optimizer=Adam()))
net.add(Layer(input_size=5, output_size=10, optimizer=Adam()))
net.add(Layer(input_size=10, output_size=20, optimizer=Adam()))
net.add(Layer(input_size=20, output_size=30, optimizer=Adam()))
net.add(Layer(input_size=30, output_size=49, optimizer=Adam()))
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
