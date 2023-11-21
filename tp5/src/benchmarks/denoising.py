import numpy as np

from src.benchmarks.plot.dae_chars_denoise_plot import denoising_plot
from src.classes.functions.ActivationFunctions import TAN_H, TAN_H_DERIVATIVE
from src.classes.functions.LossFunctions import mse, mse_prime
from src.classes.models.NeuralNetwork import NeuralNetwork
from src.classes.functions.NoiseFunctions import gaussian_noise
from src.classes.layers.DenseLayer import DenseLayer
from src.classes.optimizers.Adam import Adam
from src.data import get_characters

# Change params
EPOCHS = 10000
LEARNING_RATE = 0.0001
MEAN = 0
STD_DEVIATION = 0.5

# ADAM = 0.0001 works better

# Setup nn
net = NeuralNetwork(activation=TAN_H, activation_prime=TAN_H_DERIVATIVE, optimizer=Adam,
                    architecture=[35, 25, 25, 2, 25, 25, 35], learning_rate=LEARNING_RATE)

characters = get_characters()

noisy_characters = gaussian_noise(characters, MEAN, STD_DEVIATION)

noisy_training_set = []
for character in noisy_characters:
    noisy_training_set.append(character)

training_expected = []
for character in characters:
    training_expected.append(character)

noisy_training_set = np.array([noisy_training_set])

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
        epochs=EPOCHS, training_expected=[training_expected], test_expected=test_expected)

# Plot
denoising_plot(net, characters, noisy_characters)

# PLUS: You can save the df it in a file
# FileUtils.save_df_in_file("latent_space", pca_df)

# so that you can use it later
# path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "benchmarks", "df_files", "latent_space.csv")
# pca_df = pd.read_csv(path)
