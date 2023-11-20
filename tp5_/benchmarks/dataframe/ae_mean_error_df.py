import numpy as np
import pandas as pd


def ae_mean_error_df(err_history: list[float]):
    error_df = pd.DataFrame({
        'epoch': np.arange(1, len(err_history) + 1),  # Assuming epochs start from 1
        'error': err_history
    })

    return error_df
