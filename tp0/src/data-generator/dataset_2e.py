import json
import os
import pandas as pd

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

CONFIG_FILE_PATH = os.path.join(os.path.dirname(
    __file__), os.pardir, 'config', 'dataset_2e.json')
CSV_PATH = os.path.join(os.path.dirname(__file__),
                        os.pardir, 'output', 'dataset_2e.csv')
POKEMON_JSON_PATH = os.path.join(os.path.dirname(
    __file__), os.pardir, os.pardir, 'pokemon.json')

# Load config
with open(CONFIG_FILE_PATH) as f:
    config = json.load(f)
    CATCH_ATTEMPTS = config["params"]["catch_attempts"]
    POKEMON_NAME = config["pokemon"]["name"]
    POKEMON_HP = config["pokemon"]["hp"]
    LEVEL_RANGE = config["params"]["level_range"]
    POKEBALLS = config["params"]["pokeballs"]
    STATUS_EFFECTS = config["params"]["status_effect"]

factory = PokemonFactory(POKEMON_JSON_PATH)

data_rows = []
for level in range(LEVEL_RANGE[0], LEVEL_RANGE[1] + 1):
    for pokeball in POKEBALLS:
        for status_effect in STATUS_EFFECTS:
            pokemon = factory.create(
                POKEMON_NAME, level, StatusEffect[status_effect], POKEMON_HP)
            for _ in range(CATCH_ATTEMPTS):
                catch_result = attempt_catch(pokemon, pokeball)
                data_row = {"pokemon": pokemon.name, "level": level, "status_effect": status_effect,
                            "pokeball": pokeball, "catch_result": catch_result[0]}
                data_rows.append(data_row)

df = pd.DataFrame(data_rows)

df.to_csv(CSV_PATH, index=False)

print("Data saved to:", CSV_PATH)
