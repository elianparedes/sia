import sys
import os
import numpy as np
from Config import Config
from src.utils.ExerciseUtils import ExerciseUtils 
from src.benchmarks.plot.TestAndTrainingErrors import test_and_training_errors_plot
from src.benchmarks.plot.SplitErrors import split_ratio_errors_plot
from src.benchmarks.plot.StepPlot import and_step_plot, xor_step_plot
from src.benchmarks.numbers_metrics import number_metrics
from src.ui.Whiteboard import Whiteboard
from src.test.TestNeuralNetwork import neural_network_test, test_digits
from src.utils.DatasetUtils import DatasetUtils

DEFAULT_CONFIG_FILE = 'config.json'
DATA_PATH = os.path.join(os.path.dirname(__file__),
                           "Data", "TP3-ej2-conjunto.csv")

DIGITS_PATH = os.path.join(os.path.dirname(__file__),
                           "Data", "TP3-ej3-digitos.txt")


# Argument constants
ARG_HELP = "help"
ARG_FILE = "file"
ARG_WHITEBOARD = "whiteboard"

def show_help():
    print("Usage: python cli.py [-f <file_name>] [-s <qty>] [-h]")
    print(f"-f, --{ARG_FILE}    <file_name>")
    print("\tThe name of the config file. It defaults to `config.json`.")
    print(f"-h, --{ARG_HELP}")
    print("\tPrint usage.")
    print(f"-w, --{ARG_WHITEBOARD}")
    print("\tOpen number recognition whiteboard.")
    return


def main():
    args = {ARG_HELP: False, ARG_FILE: None, ARG_WHITEBOARD: False}

    # Parse command-line arguments
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]

        if arg in ("-f", f"--{ARG_FILE}"):
            args[ARG_FILE] = sys.argv[i] if i < len(sys.argv) else None
        elif arg in ("-h", f"--{ARG_HELP}"):
            args[ARG_HELP] = True
        elif arg in ("-w", f"--{ARG_WHITEBOARD}"):
            args[ARG_WHITEBOARD] = True

        i += 1

    config_file = args[ARG_FILE] if args[ARG_FILE] is not None else DEFAULT_CONFIG_FILE
    help_flag = args[ARG_HELP]

    if help_flag:
        show_help()
        exit(0)
    else:  
        config = Config(config_file)

        if 'and_steps' in config.run:
            and_step_plot(
                config.plot['and_steps']['training_set'],
                config.plot['and_steps']['training_expected'],
                config.plot['and_steps']['speed'],
                config.plot['and_steps']['frame_duration']
            )

        if 'xor_steps' in config.run:
            xor_step_plot(
                config.plot['xor_steps']['training_set'],
                config.plot['xor_steps']['training_expected'],
                config.plot['xor_steps']['speed'],
                config.plot['xor_steps']['frame_duration']
            )

        if 'test_and_training_error' in config.run:
            inputs, expected = ExerciseUtils.load_ex2_file(DATA_PATH)
            test_and_training_errors_plot(
                inputs,
                expected,
                config.plot['test_and_training_errors']['bias'],
                config.plot['test_and_training_errors']['learning_rate'],
                config.plot['test_and_training_errors']['batch_amount'],
                config.plot['test_and_training_errors']['epsilon'],
                config.plot['test_and_training_errors']['max_epoch'],
                config.plot['test_and_training_errors']['activation_function'][0],
                config.plot['test_and_training_errors']['activation_function'][1],
                config.plot['test_and_training_errors']['normalize_range']
            )

        if 'split_ratio_errors' in config.run:
            inputs, expected = ExerciseUtils.load_ex2_file(DATA_PATH)
            split_ratio_errors_plot(
                inputs,
                expected,
                config.plot['split_ratio_errors']['bias'],
                config.plot['split_ratio_errors']['learning_rate'],
                config.plot['split_ratio_errors']['batch_amount'],
                config.plot['split_ratio_errors']['epsilon'],
                config.plot['split_ratio_errors']['max_epoch'],
                config.plot['split_ratio_errors']['activation_function'][0],
                config.plot['split_ratio_errors']['activation_function'][1],
                config.plot['split_ratio_errors']['normalize_range']
            )

        if 'number_metrics' in config.run:
            number_metrics(
                float(config.plot['number_metrics']['epsilon']),
                float(config.plot['number_metrics']['learning_rate']),
                int(config.plot['number_metrics']['max_epoch']),
                int(config.plot['number_metrics']['batch_amount']),
                float(config.plot['number_metrics']['noise']),
            )

        if args[ARG_WHITEBOARD] is True:
            print("Training the neural network...")
            w, network = test_digits()

            print("Opening number recognition whiteboard...")
            Whiteboard(on_recognize= lambda x: network.test_forward_propagation_custom(np.array(x).reshape(35), w)).show()

if __name__ == "__main__":
    main()