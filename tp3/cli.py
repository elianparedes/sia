import sys
import os
from Config import Config
from src.utils.ExerciseUtils import ExerciseUtils 
from src.benchmarks.plot.TestAndTrainingErrors import test_and_training_errors_plot
from src.benchmarks.plot.StepPlot import and_step_plot, xor_step_plot

DEFAULT_CONFIG_FILE = 'config.json'
DATA_PATH = os.path.join(os.path.dirname(__file__),
                           "Data", "TP3-ej2-conjunto.csv")

# Argument constants
ARG_HELP = "help"
ARG_FILE = "file"

def show_help():
    print("Usage: python cli.py [-f <file_name>] [-s <qty>] [-h]")
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
            i += 1
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

        and_step_plot(
            config.plot['and_steps']['training_set'],
            config.plot['and_steps']['training_expected'],
            config.plot['and_steps']['speed'],
            config.plot['and_steps']['frame_duration']
        )
        
        xor_step_plot(
            config.plot['xor_steps']['training_set'],
            config.plot['xor_steps']['training_expected'],
            config.plot['xor_steps']['speed'],
            config.plot['xor_steps']['frame_duration']
        )

        inputs, expected = ExerciseUtils.load_ex2_file(DATA_PATH)
        test_and_training_errors_plot(
            inputs,
            expected,
            config.plot['test_and_training_errors']['bias'],
            config.plot['test_and_training_errors']['learning_rate'],
            config.plot['test_and_training_errors']['epsilon'],
            config.plot['test_and_training_errors']['max_epoch']
        )
        


if __name__ == "__main__":
    main()