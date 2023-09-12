import math
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def seed_quantity_for_characters(agg_data, title, xaxis, yaxis):
    characters = agg_data['character'].unique()
    quantities = agg_data['quantity'].unique()

    colors = ['blue', 'red', 'green', 'purple', 'yellow']

    grid_size = math.ceil(math.sqrt(len(characters)))

    fig = make_subplots(rows=grid_size, cols=grid_size, subplot_titles=characters)

    for idx, character in enumerate(characters):
        row, col = divmod(idx, grid_size)
        row += 1
        col += 1

        subset = agg_data[agg_data['character'] == character]

        for quantity, color in zip(quantities, colors):
            data = subset[subset['quantity'] == quantity]
            fig.add_trace(go.Bar(
                x=[quantity],
                y=data['mean'],
                error_y=dict(type='data', array=data['std'], visible=True),
                name=quantity.__str__(),
                marker=dict(color=color),
                showlegend=(idx == 0),
            ), row=row, col=col)

        if col == 1:
            fig.update_yaxes(title_text=yaxis, row=row, col=col)
        fig.update_xaxes(title_text=xaxis, row=row, col=col)

    fig.update_layout(title_text=title)
    fig.show()


def seed_quantity_by_fitness_plot(df):
    agg_data = df.groupby(['character', 'quantity'])['fitness'].agg(['mean', 'std']).reset_index()
    title = 'Average Fitness by Seed Quantity'
    seed_quantity_for_characters(agg_data, title, 'Seed quantity', 'Fitness')


def seed_quantity_by_generation_plot(df):
    agg_data = df.groupby(['character', 'quantity'])['generation'].agg(['mean', 'std']).reset_index()
    title = 'Average Generation Count by Seed Quantity'
    seed_quantity_for_characters(agg_data, title, 'Seed quantity', 'Generation')
