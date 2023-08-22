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
In order to run the benchmarks.py you will need to configure the `config.json` file. 
The structure of the file is as follows:
```json
"benchmarks": {
	"dataframe": Do you want to generate a dataframe? If false, then a .csv 'tp1/output/' MUST be provided with the name `<benchmark>_df.csv`,
	"export_csv": Do you want to export it into a .csv file?,
	"plot": Do you want to make a plot?,
	"run": [<benchmark>] List containing all the benchmarks which are to be generated.
},
"settings": {
	MUST contain all the benchmarks provided in the "run" field. Each one of them has the same options:
	"<benchmark>": {
		"deadlocks": [true|false] Do you want to run it with deadlocks? Some benchmarks might ignore this option, but it is mandatory nonetheless.
		"algorithms": [<algorithm>] List containing the algorithms to be run. If not specified then all algorithms are executed.
		"maps": [<map>] List containing all the maps to be run. If not specified then all maps are executed. Maps can be found under the `resources/maps` folder.
	},
}
```
<benchmark>: heatmap, algorithms, heuristic
<algorithm>: bfs, dfs, a-star, global_greedy, local_greedy
<map>: any map under the `resources/maps` folder. If you wish to add new maps, they MUST be under the `resources/maps` folder. Maps MUST be a .txt file. 
