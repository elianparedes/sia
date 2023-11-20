import numpy as np

from benchmarks.plot.denoising_plot import denoising_plot
from classes.ActivationFunctions import TAN_H, TAN_H_DERIVATIVE, SIGMOID, SIGMOID_DERIVATIVE, TAN_H, TAN_H_DERIVATIVE
from classes.LossFunctions import mse, mse_prime
from classes.NeuralNetwork import NeuralNetwork
from classes.NoiseFunctions import gaussian_noise
from classes.layer.Layer import Layer
from classes.optimizers.Adam import Adam
from classes.utils.TrainingUtils import TrainingUtils
from data import get_characters

# Change params
EPOCHS = 1000000
LEARNING_RATE = 0.001
MEAN = 0
STD_DEVIATION = 0.1

# ADAM = 0.0001 works better

# Setup nn
net = NeuralNetwork()

net.add(Layer(35, 64, TAN_H, TAN_H_DERIVATIVE, Adam()))
net.add(Layer(64, 64, TAN_H, TAN_H_DERIVATIVE, Adam()))
net.add(Layer(64, 64, TAN_H, TAN_H_DERIVATIVE, Adam()))
net.add(Layer(64, 64, TAN_H, TAN_H_DERIVATIVE, Adam()))
net.add(Layer(64, 2, TAN_H, TAN_H_DERIVATIVE, Adam()))
net.add(Layer(2, 64, TAN_H, TAN_H_DERIVATIVE, Adam()))
net.add(Layer(64, 64, TAN_H, TAN_H_DERIVATIVE, Adam()))
net.add(Layer(64, 64, TAN_H, TAN_H_DERIVATIVE, Adam()))
net.add(Layer(64, 64, TAN_H, TAN_H_DERIVATIVE, Adam()))
net.add(Layer(64, 35, TAN_H, TAN_H_DERIVATIVE, Adam()))


characters = get_characters()

noisy_characters = gaussian_noise(characters, MEAN, STD_DEVIATION)

noisy_training_set = []
for character in noisy_characters:
    noisy_training_set.append([character])

training_expected = []
for character in characters:
    training_expected.append([character])

noisy_training_set = np.array(noisy_training_set)

test_set = np.array(gaussian_noise(characters.copy(), MEAN, STD_DEVIATION))

test_expected = np.array(characters.copy())


print(np.shape(noisy_training_set))
print(np.shape(training_expected))
print('--------------')
print(np.shape(test_set))
print(np.shape(test_expected))


# Train nn
net.use(mse, mse_prime)
net.fit(training_set=noisy_training_set, test_set=test_set,
        epochs=EPOCHS, learning_rate=LEARNING_RATE, training_expected=training_expected, test_expected=test_expected)

# Plot
denoising_plot(net, characters)

## PLUS: You can save the df it in a file
# FileUtils.save_df_in_file("latent_space", pca_df)

## so that you can use it later
# path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "benchmarks", "df_files", "latent_space.csv")
# pca_df = pd.read_csv(path)
