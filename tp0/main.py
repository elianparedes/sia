import sys
import json
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect


if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")
    with open(f"{sys.argv[1]}","r") as f:
        config = json.load(f)
        ball = config["pokeball"]
        pokemon = factory.create(config["pokemon"], 100, StatusEffect.NONE, 1)
    print("No noise: ", attempt_catch(pokemon, ball))
    for _ in range(10):
        print("Noisy: ", attempt_catch(pokemon, ball, 0.15))
