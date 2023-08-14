import json
import matplotlib.pyplot as plt
import numpy as np
import sys

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")
    with open(f"{sys.argv[1]}", "r") as f:
        effects = [e.value[0] for e in StatusEffect]
        healths = {e: [] for e in range(10, 100, 10)}
        config = json.load(f)
        ball = config["pokeball"]
        fig, ax = plt.subplots(layout='constrained')
        for w in StatusEffect:
            count = 0
            for i in range(10, 100, 10):
                pokemon = factory.create(config["pokemon"], 100, w, i / 100)
                for _ in range(1000):
                    catch, _ = attempt_catch(pokemon, ball, 0.15)
                    if catch:
                        count += 1
                healths[i].append(count)
                count = 0
    x = np.arange(len(effects))  # the label locations
    width = 0.1  # the width of the bars
    multiplier = 0
    for attribute, measurement in healths.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=4)
        multiplier += 1
    ax.set_ylabel('Captures')
    ax.set_title('Captures by Status Effect and Health')
    ax.set_xticks(x + width, effects)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 800)
    plt.show()
