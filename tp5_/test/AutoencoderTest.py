import numpy as np
import random
import string

from data.fonts import get_characters
from classes.optimizers.Adam import Adam
from classes.ActivationFunctions import SIGMOID, SIGMOID_DERIVATIVE, TAN_H, TAN_H_DERIVATIVE
from classes.LossFunctions import mse_prime, mse
from classes.NeuralNetwork import NeuralNetwork
from classes.layer.Layer import Layer

def generate_batches(characters, batch_size):
    batch_size = max(batch_size, 1)
    
    num_complete_batches, remainder = divmod(len(characters), batch_size)

    random.shuffle(characters)

    batches = [characters[i * batch_size:(i + 1) * batch_size] for i in range(num_complete_batches)]

    if remainder:
        last_batch = characters[num_complete_batches * batch_size:]
        random_fill = random.sample(characters, batch_size - remainder)
        last_batch.extend(random_fill)
        batches.append(last_batch)

    return batches
    
# network
net = NeuralNetwork()
net.add(Layer(35, 30, TAN_H, TAN_H_DERIVATIVE, Adam()))
net.add(Layer(30, 20, TAN_H, TAN_H_DERIVATIVE, Adam()))
net.add(Layer(20, 10,TAN_H, TAN_H_DERIVATIVE, Adam()))
net.add(Layer(10, 5,TAN_H, TAN_H_DERIVATIVE, Adam()))
net.add(Layer(5, 2, TAN_H, TAN_H_DERIVATIVE, Adam()))
net.add(Layer(2, 5, TAN_H, TAN_H_DERIVATIVE, Adam()))
net.add(Layer(5, 10,TAN_H, TAN_H_DERIVATIVE, Adam()))
net.add(Layer(10, 20, TAN_H, TAN_H_DERIVATIVE, Adam()))
net.add(Layer(20, 30,TAN_H, TAN_H_DERIVATIVE, Adam()))
net.add(Layer(30, 35,TAN_H, TAN_H_DERIVATIVE, Adam()))
characters = get_characters()

training_set = np.array(generate_batches(characters.copy(), 10))
training_expected = training_set.copy()

test_set = np.array(characters.copy())
test_expected = characters.copy()

# train
net.use(mse, mse_prime)
net.fit(training_set, test_set, 1000000000, 0.0005, training_expected, test_expected)


# test
out = net.predict(test_set)[0]
for i in range(len(test_set)):
    print("--------------------------------")
    print("Expected",test_set[i])
    print("--------------------------------")
    print("Result",out[i])

