# TP3 - Simple and Multilayer Perceptrons
## Requirements
- Python3
- Plotly
- Pandas
- NumPy
- Sklearn

## Running the project
In order to run the project you need to first complete de `config.json` file. After that, you can  use the `cli` to run the project.

### config.json
See `options.json` to know how to fill out `config.json`.
_Note on plots_: 
- Plots which use a kohonen network need you to fill the "kohonen" element in the json (these plots are: country_association, umatrix, umatrix_byvar).
- Plots which use the hopfield model need you to fill the "hopfield" element in the json (these plots are: letters, big_letters, energy).

### cli.py
```bash
Usage: python cli.py [-f <file_name>] [-h]
-f, --file    <file_name>
        The name of the config file. It defaults to `config.json`.
-h, --help
        Print usage.
```
