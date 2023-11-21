import numpy as np
import pandas as pd


def vae_latent_space_df(sampled_latent):
    # Reshape the array to have one row per point
    reshaped_data = np.array(sampled_latent).reshape(-1, 2)

    # Create a DataFrame
    columns = ['Dimension_1', 'Dimension_2']
    latent_df = pd.DataFrame(reshaped_data, columns=columns)

    # Add a 'Group' column based on the original shape
    latent_df['Group'] = np.repeat(np.arange(1, 33), 1000)

    return latent_df
