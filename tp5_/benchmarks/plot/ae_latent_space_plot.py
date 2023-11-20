import plotly.graph_objects as go
from pandas import DataFrame


def ae_latent_space_plot(pca_df: DataFrame):

    # Creating a scatter plot
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=pca_df['PCA 1'],
        y=pca_df['PCA 2'],
        mode='markers',
        marker=dict(color='Blue', size=20),
        text=pca_df['Character'],
        name='PCA Plot'
    ))

    # Add annotations for character labels
    for i, row in pca_df.iterrows():
        fig.add_annotation(
            x=row['PCA 1'],
            y=row['PCA 2'],
            text=row['Character'],
            showarrow=False,
            font=dict(size=20, color='black')
        )

    # Customize layout
    fig.update_layout(
        title='2D Visualization of Latent Space (PCA) with Characters',
        xaxis=dict(title='PCA 1'),
        yaxis=dict(title='PCA 2'),
    )

    # Show the plot
    fig.show()

