from src.classes.networks.Hopfield import Hopfield


def hopfield_progression_df(epochs, patterns, input_state, grid_size):
    network = Hopfield(patterns, input_state)
    heatmap_patterns = []
    __convert_patterns_to_heatmap(network, heatmap_patterns, grid_size)
    heatmaps_by_epoch = []
    __convert_states_to_heatmap(network, heatmaps_by_epoch, grid_size)
    for i in range(0, epochs):
        network.train_epoch()
        __convert_states_to_heatmap(network, heatmaps_by_epoch, grid_size)
    return heatmaps_by_epoch, heatmap_patterns


def __convert_states_to_heatmap(network, heatmaps, grid_size):
    heatmap = [[] for _ in range(grid_size)]
    i = 0
    j = 0
    for state in network.get_states():
        heatmap[i].append(state)
        j += 1
        if j % grid_size == 0:
            i += 1
            j = 0
    heatmaps.append(heatmap)


def __convert_patterns_to_heatmap(network, heatmaps, grid_size):
    for pattern in network.patterns:
        heatmap = [[] for _ in range(grid_size)]
        i = 0
        j = 0
        for value in pattern:
            heatmap[i].append(value)
            j += 1
            if j % grid_size == 0:
                i += 1
                j = 0
        heatmaps.append(heatmap)
