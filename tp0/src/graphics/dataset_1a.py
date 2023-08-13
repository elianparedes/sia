import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

CATCH_ATTEMPTS = 100
CSV_PATH = "../output/dataset_1a.csv"

df = pd.read_csv(CSV_PATH)
pokeballs = df["Pokeball"].unique()
pokemon_names = df["Pokemon"].unique()

catch_probabilities = {}

for pokeball in pokeballs:
    catch_probabilities[pokeball] = ()

for pokemon in pokemon_names:
    for pokeball in pokeballs:
        pokemon_data = df[df["Pokemon"] == pokemon]
        pokemon_pokeball_data = pokemon_data[pokemon_data["Pokeball"] == pokeball]
        catch_results = pokemon_pokeball_data[pokemon_pokeball_data["Catch Result"] == True]
        catch_probabilities[pokeball] += (len(catch_results)/CATCH_ATTEMPTS, )

# plot
x_spacing = 1.3
x = np.linspace(0, (len(pokemon_names) - 1) * x_spacing, len(pokemon_names))
width = 0.25
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in catch_probabilities.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

ax.set_ylabel('Capture rate')
ax.set_title('Capture rate for each Pokeball')
ax.set_xticks(x + width, pokemon_names)
ax.legend(loc='upper right', ncols=3)
ax.set_ylim(0, 0.8)

plt.show()