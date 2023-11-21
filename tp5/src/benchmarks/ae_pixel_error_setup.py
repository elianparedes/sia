import os

import numpy as np
import pandas as pd

from src.Config import Config
from src.benchmarks.dataframe.ae_error_df import ae_error_df
from src.benchmarks.plot.ae_pixel_error_plot import ae_pixel_error_plot
from src.classes.functions.LossFunctions import mse_prime, mse
from src.classes.models.NeuralNetwork import NeuralNetwork
from src.classes.utils.FileUtils import FileUtils
from src.classes.utils.TrainingUtils import TrainingUtils
from src.data import get_characters


def ae_true_error_setup(config: Config):
    config_ae = config.autoencoder

    if config.load_dataframe is True:
        path = os.path.join(os.path.dirname(__file__), os.pardir, "benchmarks", "df_files", "true_or_pixel_error.csv")
        pca_df = pd.read_csv(path)
    else:
        net = NeuralNetwork(activation=config_ae['activation'], activation_prime=config_ae['activation_prime'],
                            optimizer=config_ae['optimizer'], architecture=config_ae['layers'])
        characters = get_characters()

        training_set = np.array(TrainingUtils.generate_batches(characters.copy(), config_ae['batch_size']))
        training_expected = training_set.copy()

        test_set = np.array(characters.copy())
        test_expected = characters.copy()

        # Train nn
        net.use(mse, mse_prime)
        err_history, computed_err = net.fit(training_set, test_set, config_ae['epochs'], training_expected,
                                            test_expected)

        # Create dataframe
        pca_df = ae_error_df(err_history, computed_err)

    if config.save_dataframe is True:
        FileUtils.save_df_in_file("true_and_pixel_error", pca_df)

    # Plot
    ae_pixel_error_plot(pca_df)
