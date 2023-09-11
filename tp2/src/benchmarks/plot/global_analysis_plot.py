import pandas as pd
import os
import math
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

from src.utils.ConfigUtils import ConfigUtils


def global_analysis_avg(df):
    fig = make_subplots(rows=2, cols=2, subplot_titles=list(ConfigUtils.CHARACTERS.keys()))

    # Crear un diccionario para almacenar los colores asociados a cada tipo
    tipo_colores = {
        'strength': 'red',
        'health': 'blue',
        'intelligence': 'green',
        'agility': 'purple',
        'endurance': 'orange'
    }
    added_type_names = set()

    for idx, char in enumerate(ConfigUtils.CHARACTERS.keys()):
        subset = df[df['character'] == char]

        row = (idx // 2) + 1
        col = (idx % 2) + 1

        for tipo, color in tipo_colores.items():
            rslt = subset[subset['type'] == tipo]

            # Comprobar si el nombre del tipo ya se agregó a la leyenda
            if tipo not in added_type_names:
                # Crear la traza para cada tipo
                traza = go.Scatter(
                    x=rslt['iteration'],
                    y=rslt['value'],
                    name=tipo,  # Usar el tipo como nombre
                    line=dict(color=color),  # Mantener el color
                    showlegend=True
                )
                # Registrar el nombre del tipo en el conjunto de nombres agregados
                added_type_names.add(tipo)
            else:
                traza = go.Scatter(
                    x=rslt['iteration'],
                    y=rslt['value'],
                    name=tipo,  # Usar el tipo como nombre
                    line=dict(color=color),  # Mantener el color
                    showlegend=False
                )
            fig.add_trace(traza, row=row, col=col)

    fig.update_layout(height=600, width=800, title_text=title)
    fig.show()
