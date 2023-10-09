import os
import signal
import sys
import shutil
import inquirer as inquirer
from utils.Utils import Utils

DEFAULT_PACKAGES = ['classes', 'utils', 'benchmarks']
ROOT_DIRECTORY = []


class ProjectBuilder:

    @staticmethod
    def with_package(package: str):
        print(f"{package.capitalize()} package?")
        response = input("Enter 'yes' or 'no': ").lower().strip()
        while response not in ['yes', 'no', 'y', 'n']:
            response = input("Invalid input. Please enter 'yes' or 'no': ").lower().strip()
        if response in ['yes', 'y']:
            return True

        return False

    @staticmethod
    def clean_directories():
        if not ROOT_DIRECTORY:
            return
        print("Cleaning directories...")
        if os.listdir(ROOT_DIRECTORY[0]):  # Check if directory is not empty
            shutil.rmtree(ROOT_DIRECTORY[0])
        else:
            os.rmdir(ROOT_DIRECTORY[0])

    @staticmethod
    def signal_handler(signum, frame):
        print(f"\nCaught signal {signum}, cleaning up...")
        ProjectBuilder.clean_directories()
        sys.exit(1)



    @staticmethod
    def create_project():
        signal.signal(signal.SIGINT, ProjectBuilder.signal_handler)
        signal.signal(signal.SIGTERM, ProjectBuilder.signal_handler)

        try:
            project_name = input("Project name: ")
            while os.path.exists(project_name):
                print(f"Project {project_name} already exists\n")
                project_name = input("Project name: ")
            os.mkdir(project_name)
            ROOT_DIRECTORY.append(project_name)

            mode_prompt = [
                inquirer.List('mode',
                              message="Choose the configuration for the project:",
                              choices=['Default - [classes, benchmarks, utils]', 'Custom'],
                              carousel=True
                              ),
            ]

            mode = inquirer.prompt(mode_prompt)
            mode = mode['mode'].split(' - ')[0].lower()

            src_path = os.path.join(project_name, "src")
            Utils.create_package(src_path)

            for package in DEFAULT_PACKAGES:
                if (mode == 'default') or ProjectBuilder.with_package(package):
                    Utils.create_package(os.path.join(src_path, package))

            benchmarks_path = os.path.join(src_path, "benchmarks")
            if os.path.exists(benchmarks_path):
                Utils.create_package(os.path.join(benchmarks_path, "dataframe"))
                Utils.create_package(os.path.join(benchmarks_path, "plot"))

            response = 'yes'
            while response not in ['no', 'n']:
                print("Add a new package?")
                response = input("Enter 'yes' or 'no': ").lower().strip()
                while response not in ['yes', 'no', 'y', 'n']:
                    response = input("Invalid input. Please enter 'yes' or 'no': ").lower().strip()
                if response in ['yes', 'y']:
                    package = input("Enter package name: ")
                    Utils.create_package(os.path.join(src_path, package))

        except Exception as e:
            print(f"Exception: {e}")
            ProjectBuilder.clean_directories()
