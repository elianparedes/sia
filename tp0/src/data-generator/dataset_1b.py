import json
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from src.pokemon import PokemonFactory, StatusEffect, Pokemon
from src.catching import attempt_catch

def solve_1b():
    factory = PokemonFactory("pokemon.json")
    with open("./src/config/dataset_1b.json") as f:
        config = json.load(f)
        pokemons_names = config["pokemons"]
        iterations = config["iterations"]
        balls = config["balls"]
        base_ball = config["base_ball"]
    
    pokemons = []
    for name in pokemons_names:
        pokemon = factory.create(name, 100, StatusEffect.NONE, 1)
        pokemons.append(pokemon)

    balls_catch_rates = {}
    for ball in balls:
        balls_catch_rates[ball] = pokemon_catch_rates(pokemons,ball,iterations)
    export_csv_results(balls_catch_rates,base_ball)

    normalized_catch_rates = {}
    for ball, pokemons in balls_catch_rates.items():
        normalized_catch_rates[ball] = {pokemon: rate/balls_catch_rates[base_ball][pokemon] for pokemon, rate in pokemons.items()}

    del normalized_catch_rates[base_ball]
    balls.remove(base_ball)

    export_graph(normalized_catch_rates,balls,pokemons_names)

   

def export_graph(normalized_catch_rates,balls,pokemons):

    with open("./src/config/dataset_1b.json") as f:
        config = json.load(f)
        bar_colors = config["colors"]
        output_path = config["output_path"]

    bar_width = 1/(len(balls)+1)
    r = np.arange(len(pokemons))
    for i, ball in enumerate(balls):
        plt.bar(r, [normalized_catch_rates[ball][pokemon] for pokemon in pokemons],
                color=bar_colors[i], width=bar_width, edgecolor='grey', label=ball)
        r = r + bar_width

    plt.xlabel('Pokemons', fontweight='bold')
    plt.xticks([r + bar_width for r in range(len(pokemons))], pokemons)
    plt.ylabel('Effectiveness Relative to Base Pokeball')
    plt.legend()

    plt.savefig(output_path)
    
def export_csv_results(balls_catch_rates, base_ball):
    header = ['PokeballType'] + list(balls_catch_rates[base_ball].keys())
    with open('./src/output/dataset_1b.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)  # Writing the header
        for pokeball, rates in balls_catch_rates.items():
            writer.writerow([pokeball] + list(rates.values()))

def pokeball_avg(rates: list[float]):
    return sum(rates) / len(rates)

def pokemon_catch_rates(pokemons: list[Pokemon], ball: str, iterations: int) -> dict[{str,float}]:
    catch_rates = {}
    for pokemon in pokemons:
        catched = 0
        for _ in range(iterations):
            success,_ = attempt_catch(pokemon, ball)
            catched += success
        catch_rates[pokemon._name] = (catched/iterations)
    return catch_rates