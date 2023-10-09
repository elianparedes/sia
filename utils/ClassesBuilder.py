import os
import inquirer as inquirer
from utils.Utils import Utils


class ClassesBuilder:

    @staticmethod
    def __create_abstract_class(class_name, class_package):
        content = f"""from abc import ABC, abstractmethod\n\n\nclass {class_name}(ABC):\n\tpass\n"""

        file_path = os.path.join(class_package, f"{class_name}.py")
        with open(file_path, "w") as file:
            file.write(content)

    @staticmethod
    def __create_class(class_name, class_package, abs_class=None):

        if abs_class:
            parts =  class_package.split(os.sep)[1:]
            relative_import_path = ".".join(parts) + "." + abs_class
            import_statement = f"from {relative_import_path} import {abs_class}\n\n"
        else:
            import_statement = ""

        inheritance_str = f"({abs_class})" if abs_class else ""
        content = f"""{import_statement}class {class_name}{inheritance_str}:\n\tpass\n"""

        file_path = os.path.join(class_package, f"{class_name}.py")
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return

        with open(file_path, "w") as file:
            file.write(content)

    @staticmethod
    def create_classes():
        project_path = input("Type the project path: ")
        if not os.path.exists(project_path):
            raise Exception(f"Project {project_path} does not exists")

        options_prompt = [
            inquirer.List('option',
                          message="Which path you want for your classes package: ",
                          choices=['Default - /src/classes/', 'Custom'],
                          carousel=True
                          ),
        ]

        option = inquirer.prompt(options_prompt)
        option = option['option'].split(' - ')[0].lower()

        classes_path = os.path.join(os.path.join(project_path, "src"), "classes")

        if option == 'custom':
            path = input("Type your custom path relative to project: ")
            classes_path = os.path.join(project_path, path)

        package = input("Type your package name: ")
        package_path = os.path.join(classes_path, package)
        Utils.create_package(package_path)

        options_prompt = [
            inquirer.List('option',
                          message="With abstract class?: ",
                          choices=['yes', 'no'],
                          carousel=True
                          ),
        ]
        option = inquirer.prompt(options_prompt)
        option = option['option']
        print(option)

        if option == 'yes':
            abstract = input("Type your abstract class name: ")
            while not Utils.is_valid_identifier(abstract):
                print("Invalid class indentifier\n")
                abstract = input("Type your abstract class name: ")
            ClassesBuilder.__create_abstract_class(abstract, package_path)

        classes_input = input("Enter class names separated by comma: ").strip()
        class_names = [name.strip() for name in classes_input.split(",")]

        for class_name in class_names:
            if Utils.is_valid_identifier(class_name):
                if option == 'yes':
                    ClassesBuilder.__create_class(class_name, package_path, abs_class=abstract)
                else:
                    ClassesBuilder.__create_class(class_name, package_path)
            else:
                print(f"'{class_name}' is not a valid Python identifier or is a reserved keyword.")
