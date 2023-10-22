from src.classes.networks.Hopfield import Hopfield


def letters_progression_df(epochs, patterns, input_state):
    network = Hopfield(patterns, input_state)
    letters_arrays = []
    letter_arrays = [[] for _ in range(5)]
    i = 0
    j = 0
    for state in network.get_states():
        letter_arrays[i].append(state)
        j += 1
        if j % 5 == 0:
            i += 1
            j = 0
    for i in range(0, epochs):
        network.train_epoch()
        letter_arrays = [[] for _ in range(5)]
        i = 0
        j = 0
        for state in network.get_states():
            letter_arrays[i].append(state)
            j += 1
            if j % 5 == 0:
                i += 1
                j = 0
        letters_arrays.append(letter_arrays)
    return letters_arrays
