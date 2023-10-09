import inquirer as inquirer
from utils.ProjectBuilder  import ProjectBuilder
from utils.ClassesBuilder import ClassesBuilder

option = ''

while option != 'quit':
    cli_options = [
        inquirer.List('option',
                      message='Create: ',
                      choices=['project', 'classes', 'quit'],
                      carousel=True
                      ),
    ]
    option = inquirer.prompt(cli_options)['option']

    if option == 'project':
        ProjectBuilder.create_project()
    if option == 'classes':
        ClassesBuilder.create_classes()
