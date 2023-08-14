import matplotlib.pyplot as plt
import pandas as pd

CSV_PATH = "../output/dataset_2b.csv"


def plot_by_pokeball(df, pokeball):
    plt.figure()
    # Filter the DataFrame for catch_result = True && given pokeball
    true_results = df[df["Catch Result"] == True]
    pokeball_data = true_results[true_results["Pokeball"] == pokeball]

    # Group by Pokemon and HP Percentage and count the occurrences of True
    pokemon_hp_counts = pokeball_data.groupby(["Pokemon", "HP Percentage"]).size().reset_index(name="Count")

    # Get unique Pokémon names
    unique_pokemon = pokemon_hp_counts["Pokemon"].unique()

    # Create a plot using Matplotlib
    for pokemon in unique_pokemon:
        pokemon_data = pokemon_hp_counts[pokemon_hp_counts["Pokemon"] == pokemon]
        plt.plot(pokemon_data["HP Percentage"], pokemon_data["Count"], label=pokemon)

    plt.xlabel("HP Percentage")
    plt.ylabel("Count of successful catches")
    plt.title(f"{pokeball.capitalize()} successful catches")
    plt.legend()

    plt.show()


def error_bar_plot_by_pokeballs(df, pokeballs, bin_size):
    plt.figure()

    for i, pokeball in enumerate(pokeballs):
        pokeball_data = df[df["Pokeball"] == pokeball]
        pokeball_data["HP Bin"] = pd.cut(pokeball_data["HP Percentage"], bins=bin_size)

        # Group by Pokemon, Pokeball, and HP Bin and calculate the mean and standard error
        pokemon_hp_stats = pokeball_data.groupby("HP Bin").agg(
            Mean_Count=("Catch Result", "mean"),
            Std_Err_Count=("Catch Result", "sem")
        ).reset_index()

        plt.errorbar(
            pokemon_hp_stats["HP Bin"].astype(str),
            pokemon_hp_stats["Mean_Count"],
            yerr=pokemon_hp_stats["Std_Err_Count"],
            label=pokeball
        )

    plt.xlabel("HP Percentage")
    plt.ylabel("Mean Count of successful catches")
    plt.title("Catches by Pokeball Type")
    plt.xticks(rotation=45)
    plt.legend()

    plt.show()


""" Generate plots """
df = pd.read_csv(CSV_PATH)
pokeballs = df["Pokeball"].unique()

bin_size = [0, 0.2, 0.4, 0.6, 0.8, 1.0]  # Bin boundaries here

for pokeball in pokeballs:
    plot_by_pokeball(df, pokeball)

error_bar_plot_by_pokeballs(df, pokeballs, bin_size)
