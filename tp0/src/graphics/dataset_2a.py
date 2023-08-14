import matplotlib.pyplot as plt

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

if __name__ == "__main__":
    factory = PokemonFactory("../../pokemon.json")

    counts = []
    for w in StatusEffect:
        snorlax = factory.create("snorlax", 100, w, 1)
        count = 0
        for i in range(100000):
            a, _ = attempt_catch(snorlax, "pokeball")
            if a:
                count += 1
        counts.append(count)
        print("Snorlax ", w, ": ", count)

    effect_names = [w.name for w in StatusEffect]
    normalized_counts = [count / counts[-1] for count in counts]

    plt.bar(effect_names, normalized_counts)
    for i, count in enumerate(normalized_counts):
        plt.text(i, count, f'{count:.2f}', ha='center', va='bottom', fontsize=10)
    plt.xlabel('Status Effect')
    plt.ylabel('Catch Count')
    plt.title('Catch Ratio for Different Status Effects on Snorlax')
    plt.show()
