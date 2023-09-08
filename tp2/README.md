# TP2 - Genetic Algorithms
## Requirements
- Python3
- Plotly
- Pandas
- NumPy

## Running the project
### cli.py
The project can be run using a cli, run `python cli.py -h` to see instructions on how to it:
```
Usage: python cli.py [-f <file_name>] [-s <qty>] [-h]
-f, --file    <file_name>
        The name of the config file. It defaults to `config.json`.
-s, --seed    <qty>
        Generates a random seed with <qty> individuals.
-h, --help
        Print usage.
```

### config.json
The structure of the `config.json` file can be found in the `options.json` file.
```json
{
  "character": "[warrior | archer | defender | spy]",
  "crossover": "[one-point | two-point | annular | uniform]",
  "mutation": {
    "type": "[single | limited | uniform | complete]",
    "probability": "[0-1]"
  },
  "selection": {
    "first-selection": {
      "type": "[elite | roulette | universal | boltzmann | deterministic | probabilistic]",
      "parameters": "[deterministic: {\"size\":  2} | boltzmann {\"t0\": 10, \"tc\": 5, \"k\": 2, \"generation\": 10} | else: {} ]"
    },
    "second-selection": {
      "type": "[elite | roulette | universal | boltzmann | deterministic | probabilistic]",
      "parameters": "[deterministic: {\"size\":  2} | boltzmann {\"t0\": 10, \"tc\": 5, \"k\": 2, \"generation\": 10} | else: {} ]"
    },
    "a-value": "[0-1]",
    "individuals": "[>0]"
  },
  "replacement": {
    "type": "[traditional | young]",
    "first-selection": {
      "type": "[elite | roulette | universal | boltzmann | deterministic | probabilistic]",
      "parameters": "[deterministic: {\"size\":  2} | boltzmann: {\"t0\": 10, \"tc\": 5, \"k\": 2, \"generation\": 10} | else: {} ]"
    },
    "second-selection": {
      "type": "[elite | roulette | universal | boltzmann | deterministic | probabilistic]",
      "parameters": "[deterministic: {\"size\":  2} | boltzmann: {\"t0\": 10, \"tc\": 5, \"k\": 2, \"generation\": 10} | else: {} ]"
    },
    "b-value": "[0-1]"
  },
  "cutoff": {
    "type": "max-generation | content | structure | optimum-environment",
    "parameter": "[>0]"
  },
  "seed": [
    {"strength":  20, "agility": 30, "skill": 30, "endurance": 20, "health": 50, "height": 1.7 },
    {"strength":  10, "agility": 40, "skill": 30, "endurance": 20, "health": 50, "height": 1.31 },
    {"strength":  20, "agility": 40, "skill": 20, "endurance": 20, "health": 50, "height": 1.4 },
    {"strength":  20, "agility": 30, "skill": 30, "endurance": 15, "health": 55, "height": 1.5 },
    {"strength":  20, "agility": 5, "skill": 55, "endurance": 20, "health": 50, "height": 1.6 },
    {"strength":  10, "agility": 30, "skill": 30, "endurance": 30, "health": 50, "height": 2 }
  ]
}
```
_Note_: Seed is an **optional parameter**, if you wish to generate a random seed run `cli.py` with the `-s` option.
