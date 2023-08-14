import sys
import json
import sys
from dataset_1b import solve_1b
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

sys.path.append("src/data-generator")

if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")
    with open(f"{sys.argv[1]}", "r") as f:
        config = json.load(f)
        ball = config["pokeball"]
        pokemon = factory.create(config["pokemon"], 100, getattr(StatusEffect, config["effect"]), 1)
    # print("No noise: ", attempt_catch(pokemon, ball))
    # for _ in range(10):
    #    print("Noisy: ", attempt_catch(pokemon, ball, 0.15))
    solve_1b()
