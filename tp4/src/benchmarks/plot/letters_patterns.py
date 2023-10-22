import os
import plotly.graph_objects as go
from src.utils.LettersUtils import LettersUtils

FILE_PATH = os.path.join(os.pardir, os.pardir, os.pardir, "data", "letters.csv")

def letters_patterns_plot():
    letters_map = LettersUtils.load_letters_map_from_file(FILE_PATH)

    fig = go.Figure()

    # Define size of each matrix and distance between them
    matrix_size = 5
    gap = 1

    for idx, (letter, matrix) in enumerate(letters_map.items()):
        col = idx % 7
        row = idx // 7

        x_start = col * (matrix_size + gap)
        y_start = row * (matrix_size + gap)

        for i in range(matrix_size):
            for j in range(matrix_size):
                cell_color = "black" if matrix[i][j] == 1 else "white"
                fig.add_shape(
                    type="rect",
                    x0=x_start + j,
                    y0=(4 * (matrix_size + gap) - gap) - (y_start + i + 1),  # Flip the y positioning
                    x1=x_start + j + 1,
                    y1=(4 * (matrix_size + gap) - gap) - (y_start + i),  # Flip the y positioning
                    fillcolor=cell_color,
                    line=dict(color="black", width=1)  # Border for each cell
                )

    fig.update_layout(
        xaxis=dict(range=[0, 7 * (matrix_size + gap) - gap], showgrid=False, zeroline=False),
        yaxis=dict(range=[0, 4 * (matrix_size + gap) - gap], showgrid=False, zeroline=False, scaleanchor="x"),
        # Ensure cells have the same width and height
        showlegend=False,
        plot_bgcolor="white",
        margin=dict(t=0, b=0, l=0, r=0),
        autosize=False,
        width=7 * (matrix_size + gap) * 30,  # Adjust these values based on desired cell size
        height=4 * (matrix_size + gap) * 30
    )

    fig.show()

letters_patterns_plot()