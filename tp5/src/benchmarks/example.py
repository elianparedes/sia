import numpy as np

from src.benchmarks.dataframe.ae_latent_space_df import ae_latent_space_df
from src.benchmarks.plot.ae_latent_space_plot import ae_latent_space_plot
from src.classes.ActivationFunctions import TAN_H, TAN_H_DERIVATIVE
from src.classes.LossFunctions import mse, mse_prime
from src.classes.NeuralNetwork import NeuralNetwork
from src.classes.layer.Layer import Layer
from src.classes.optimizers.Adam import Adam
from src.classes.utils.TrainingUtils import TrainingUtils
from src.data import get_characters

# Change params
EPOCHS = 10000
LEARNING_RATE = 0.0005

# Setup nn
net = NeuralNetwork(activation=TAN_H, activation_prime=TAN_H_DERIVATIVE, optimizer = Adam)
net.add(Layer(input_size=35, output_size=30,optimizer=Adam()))
net.add(Layer(input_size=30, output_size=20,optimizer=Adam()))
net.add(Layer(input_size=20, output_size=10,optimizer= Adam()))
net.add(Layer(input_size=10, output_size=5,optimizer= Adam()))
net.add(Layer(input_size=5, output_size=2,optimizer= Adam()))
net.add(Layer(input_size=2, output_size=5,optimizer= Adam()))
net.add(Layer(input_size=5, output_size=10,optimizer= Adam()))
net.add(Layer(input_size=10, output_size=20,optimizer=  Adam()))
net.add(Layer(input_size=20, output_size=30,optimizer=Adam()))
net.add(Layer(input_size=30, output_size=35,optimizer= Adam()))
characters = get_characters()

training_set = np.array(TrainingUtils.generate_batches(characters.copy(), 10))
training_expected = training_set.copy()

test_set = np.array(characters.copy())
test_expected = characters.copy()

# Train nn
net.use(mse, mse_prime)
net.fit(training_set, test_set, EPOCHS, training_expected, test_expected)

# Plot
pca_df = ae_latent_space_df(net)
ae_latent_space_plot(pca_df)

## PLUS: You can save the df it in a file
# FileUtils.save_df_in_file("latent_space", pca_df)

## so that you can use it later
# path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "benchmarks", "df_files", "latent_space.csv")
# pca_df = pd.read_csv(path)
