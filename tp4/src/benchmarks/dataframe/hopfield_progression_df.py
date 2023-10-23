from src.classes.networks.Hopfield import Hopfield


def hopfield_progression_df(epochs, patterns, input_state, grid_size):
    network = Hopfield(patterns, input_state)
    hopfield_arrays = []
    hopfield_array = [[] for _ in range(grid_size)]
    i = 0
    j = 0
    for state in network.get_states():
        hopfield_array[i].append(state)
        j += 1
        if j % grid_size == 0:
            i += 1
            j = 0
    hopfield_arrays.append(hopfield_array)
    for i in range(0, epochs):
        network.train_epoch()
        hopfield_array = [[] for _ in range(grid_size)]
        i = 0
        j = 0
        for state in network.get_states():
            hopfield_array[i].append(state)
            j += 1
            if j % grid_size == 0:
                i += 1
                j = 0
        hopfield_arrays.append(hopfield_array)
    return hopfield_arrays
