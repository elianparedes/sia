import sys
import json
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")

    with open(f"{sys.argv[1]}", "r") as f:
        counts = []
        config = json.load(f)
        ball = config["pokeball"]
        figure = plt.figure(figsize=(30, 30))
        col = 0
        row = 0
        indx = 1
        for w in StatusEffect:
                ax = figure.add_subplot(3, 2, indx, projection='3d')
                count = 0
                counts = []
                levels = np.arange(0, 100, 10)
                hps = np.arange(0, 100, 10)
                X, Y = np.meshgrid(levels, hps)
                Z = np.zeros_like(X)
                for j in range(0, 100, 10):
                    for i in range(0, 100, 10):
                        pokemon = factory.create(config["pokemon"], i, w, j / 100)
                        for _ in range(1000):
                            catch, _ = attempt_catch(pokemon, ball, 0.15)
                            if catch:
                                count += 1
                        Z[j // 10, i // 10] = count
                        count = 0

                ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
                ax.set_title(f' {config["pokemon"]} ({w})')
                ax.set_xlabel('Level')
                ax.set_ylabel('HP')
                ax.set_zlabel('Catch Count')
                ax.set_yticks(hps)
                ax.view_init(elev=10, azim=-45)
                indx += 1
    plt.tight_layout(pad=3.0)
    plt.show()