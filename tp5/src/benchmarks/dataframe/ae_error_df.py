import numpy as np
import pandas as pd


def ae_error_df(true_err: list[float], pixel_err: list[float]):
    error_df = pd.DataFrame({
        'epoch': np.arange(1, len(true_err) + 1),  # Assuming epochs start from 1
        'true_error': true_err,
        'pixel_error': pixel_err
    })

    return error_df
