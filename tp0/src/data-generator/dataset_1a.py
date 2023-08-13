import json
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
import pandas as pd

CSV_PATH = "../output/dataset_1a.csv"
POKEMON_JSON_PATH = "../../pokemon.json"
DATASET_JSON_PATH = "../config/dataset_2b.json"
CATCH_ATTEMPTS = 100

factory = PokemonFactory(POKEMON_JSON_PATH)
    
with open(DATASET_JSON_PATH) as f:
    data = json.load(f)
    POKEBALLS = data["pokeball"]
    POKEMONS = data["pokemon"]

data_rows = []
for pokemon_name in POKEMONS:
    pokemon = factory.create(pokemon_name, 100, StatusEffect.NONE, 1)
    for pokeball in POKEBALLS:
        for _ in range(CATCH_ATTEMPTS):
            catch_result = attempt_catch(pokemon, pokeball)
            data_row = {"Pokemon": pokemon_name, "Pokeball": pokeball, "Catch Result": catch_result[0]}
            data_rows.append(data_row)

df = pd.DataFrame(data_rows)
df.to_csv(CSV_PATH, index=False)