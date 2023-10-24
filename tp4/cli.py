import os
import sys

from src.Config import Config
from src.benchmarks.plot.KohonenGraphs import KohonenGraphs
from src.benchmarks.plot.OjaByEpochs import OjaEpochsGraph
from src.benchmarks.plot.hopfield_energy_plot import hopfield_energy_plot
from src.benchmarks.plot.hopfield_progression_plot import letter_progression_plot, big_letter_progression_plot
from src.classes.algorithms.KohonenAlgorithm import KohonenAlgorithm
from src.classes.networks.Kohonen import Kohonen
from src.classes.networks.Oja import Oja
from src.classes.weights.SetBased import SetBased
from src.utils import PlotNames
from src.utils.FileUtils import FileUtils

DEFAULT_CONFIG_FILE = os.path.join(os.path.dirname(__file__), 'config.json')

# Argument constants
ARG_HELP = "help"
ARG_FILE = "file"


def show_help():
    print("Usage: python cli.py [-f <file_name>] [-h]")
    print(f"-f, --{ARG_FILE}    <file_name>")
    print("\tThe name of the config file. It defaults to `config.json`.")
    print(f"-h, --{ARG_HELP}")
    print("\tPrint usage.")
    return


def main():
    args = {ARG_HELP: False, ARG_FILE: None}

    # Parse command-line arguments
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]

        if arg in ("-f", f"--{ARG_FILE}"):
            args[ARG_FILE] = sys.argv[i] if i < len(sys.argv) else None
        elif arg in ("-h", f"--{ARG_HELP}"):
            args[ARG_HELP] = True

        i += 1

    config_file = args[ARG_FILE] if args[ARG_FILE] is not None else DEFAULT_CONFIG_FILE
    help_flag = args[ARG_HELP]

    if help_flag:
        show_help()
        exit(0)
    else:
        config = Config(config_file)

        # If it is a kohonen network
        if any(s in config.run for s in (PlotNames.COUNTRY_ASSOCIATION, PlotNames.UMATRIX, PlotNames.UMATRIX_BYVAR)):
            # Train it once
            entries, countries, var_names = FileUtils.load_europe_csv()
            kohonen_config = config.algorithms['kohonen']
            if type(kohonen_config['weight_initializer']) is SetBased:
                kohonen_config['weight_initializer'] = kohonen_config['weight_initializer'](entries)
            else:
                kohonen_config['weight_initializer'] = kohonen_config['weight_initializer']()

            kohonen_network = Kohonen(len(entries[0]),
                                      kohonen_config['neuron_qty'],
                                      kohonen_config['similarity'],
                                      kohonen_config['weight_initializer'])
            KohonenAlgorithm.train(kohonen_network,
                                   entries,
                                   kohonen_config['learning_rate'],
                                   kohonen_config['radius'])

            # Plot
            if PlotNames.COUNTRY_ASSOCIATION in config.run:
                KohonenGraphs.CompleteHeatmap(kohonen_network, entries, countries)
            if PlotNames.UMATRIX in config.run:
                KohonenGraphs.PlotUMatrix(kohonen_network)
            if PlotNames.UMATRIX_BYVAR in config.run:
                KohonenGraphs.PlotUMatrixByVariable(kohonen_network, var_names)

        # Hopfield
        if any(s in config.run for s in (PlotNames.LETTERS, PlotNames.BIG_LETTERS, PlotNames.ENERGY)):
            hopfield_config = config.algorithms['hopfield']

            if PlotNames.LETTERS in config.run:
                letter_progression_plot(hopfield_config['training_letters'],
                                        hopfield_config['input'],
                                        hopfield_config['max_epochs'],
                                        hopfield_config['noise'])

            if PlotNames.BIG_LETTERS in config.run:
                big_letter_progression_plot(hopfield_config['training_letters'],
                                            hopfield_config['input'],
                                            hopfield_config['max_epochs'],
                                            hopfield_config['noise'])

            if PlotNames.ENERGY in config.run:
                hopfield_energy_plot(hopfield_config['max_epochs'],
                                     hopfield_config['training_letters'],
                                     hopfield_config['input'])

        # Oja
        if PlotNames.OJA_EPOCHS in config.run:
            oja_config = config.plots[PlotNames.OJA_EPOCHS]
            entries, scaled_data, pca = OjaEpochsGraph.setup()
            oja_network = Oja(len(entries))
            OjaEpochsGraph.plot(oja_network,
                                scaled_data,
                                oja_config['learning_rate'],
                                oja_config['max_epochs'],
                                pca[:, 0])


if __name__ == "__main__":
    main()
