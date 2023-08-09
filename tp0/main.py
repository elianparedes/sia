from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect


if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")
    snorlax = factory.create("snorlax", 100, StatusEffect.NONE, 1)
    print("No noise: ", attempt_catch(snorlax, "heavyball"))
    for _ in range(10):
        print("Noisy: ", attempt_catch(snorlax, "heavyball", 0.15))
