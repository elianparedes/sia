import pandas as pd
import json
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

CSV_PATH = "../output/dataset_2b.csv"
POKEMON_JSON_PATH = "../../pokemon.json"
DATASET_JSON_PATH = "../config/dataset_2b.json"

""" Setup """
PERCENTAGE = 100
MAX_HP_PERCENT = 100
MAX_LEVEL = 100
CATCH_ATTEMPTS = 50

factory = PokemonFactory(POKEMON_JSON_PATH)
# Load data from json file
with open(DATASET_JSON_PATH) as f:
    data = json.load(f)
    POKEBALLS = data["pokeball"]
    POKEMONS = data["pokemon"]

""" Get data """
data_rows = []
for pokeball in POKEBALLS:
    for pokemon in POKEMONS:
        for hp in range(MAX_HP_PERCENT):
            hp = hp + 1
            hp_percentage = hp / PERCENTAGE
            for _ in range(CATCH_ATTEMPTS): # Attempt multiple catches
                pokemon_instance = factory.create(pokemon, MAX_LEVEL, StatusEffect.NONE, hp_percentage)
                catch_result = attempt_catch(pokemon_instance, pokeball, 0.15)
                data_row = {"Pokemon": pokemon, "Pokeball": pokeball, "HP Percentage": hp_percentage, "Catch Result": catch_result[0]}
                data_rows.append(data_row)

df = pd.DataFrame(data_rows)

df.to_csv(CSV_PATH, index=False)

print("Data saved to:", CSV_PATH)
    