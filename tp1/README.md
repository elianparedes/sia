# TP1 - Search Methods
## Requirements
- Python3
- Plotly
- Pandas
- NumPy

## Running the project
The project can be run using a cli or, if you wish to generate plots, using the benchmarks.py script.

### Command line interface
The objective of the cli is to test-run a single algorithm.  

1. Run `cd sia/tp1`
2. Run `python cli.py -h` to see instructions on how to use the cli:
```
Usage: python cli.py -a <algorithm> -m <map_name> [-t] [-d] [-h] [-s]
-a, --algorithm
        Can be any of: 'bfs', 'dfs', 'locgreedy', 'glogreedy', 'astar'
-m, --map
        The name of a map (without the suffix .txt) inside the resources/maps folder
-t, --time
        Shows elapsed time
-d, --deadlocks
        Checks for deadlocks before running the algorithm
-s, --solution
        Shows solution at the end
-h, --help
        Print usage
```
_Note_: If you wish to add new maps, they MUST be under the `resources/maps` folder. Maps MUST be a .txt file. 

### Benchmarks.py
1. Run `cd sia/tp1`
2. Run `python -m benchmarks.benchmarks`
