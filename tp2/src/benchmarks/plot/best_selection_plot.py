import plotly.graph_objects as go
from plotly.subplots import make_subplots


def best_selection_plot(df):
    agg_data = df.groupby(['character', 'selection1', 'selection2'])['generation'].agg(['mean', 'std']).reset_index()

    character = agg_data['character'].unique()
    methods = agg_data['selection1'].unique()

    max_col_size = 3

    fig = make_subplots(rows=2, cols=max_col_size, subplot_titles=methods)

    row = 1
    col = 1
    fig.update_yaxes(title_text="Number of generations", row=row, col=col)
    for idx, method_1 in enumerate(methods):
        for method_2 in methods:
            method = (method_1, method_2)
            subset = agg_data[agg_data['character'] == character[0]]
            data = subset[subset[['selection1', 'selection2']].apply(tuple, axis=1) == method]
            diff = data['mean'] - data['std']
            is_positive = diff >= 0

            array = data['std'] if is_positive.all() else data['std'] + (-diff)
            arrayminus = data['std'] if is_positive.all() else data['std'] - (-diff)

            legend_name = f'{method[1]}'
            fig.add_trace(go.Bar(
                x=[legend_name],
                y=data['mean'],
                error_y=dict(type='data', array=array, arrayminus=arrayminus, visible=True, symmetric=False),
                name=legend_name,
                showlegend=(idx == 0),
            ), row=row, col=col)

        if col == 3:
            row += 1
            col = 1
            fig.update_yaxes(title_text="Number of generations", row=row, col=col)
        else:
            col += 1

    fig.update_layout(title_text=f'Average Generations to Max Fitness by Selections ({character[0]})')
    fig.show()
