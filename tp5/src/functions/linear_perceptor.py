import random
import sys
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from src.classes.perceptron.Step import Step

values = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
expected = [-1, -1, -1, 1]
learning_rate = 0.1
ws = []

def normalized_input(input):
    return [[1] + row for row in input]
def linear_perceptor():
    i = 0
    limit = 1000000
    w = initialize_weights()
    perceptron = Step(normalized_input(values), expected, w, learning_rate)
    ws.append(w)
    min_error = sys.maxsize
    w_min = None
    while min_error > 0 and i < limit:
        mu = random.randint(0, len(values) - 1)
        excitement = perceptron.excitement(mu)
        activation = perceptron.activation(excitement)
        w = perceptron.update_weights(activation, mu)
        ws.append(w)
        error = perceptron.error()
        if error < min_error:
            min_error = error
            w_min = w
        i += 1
    return w_min


# Scalar product
def compute_excitement(w, x):
    return w[0] + w[1] * x[0] + w[2] * x[1]


# Activation function
def compute_activation(excitement):
    return 1 if excitement > 0 else -1


# Simulation
def compute_error(w):
    wrong = 0
    for i in range(0, len(values)):
        if compute_activation(compute_excitement(w, values[i])) != expected[i]:
            wrong += 1
    return wrong / len(values)


# Random weights
def initialize_weights():
    w = []
    for i in range(0, 3):
        w.append(random.uniform(-1, 1))
    return w


print(linear_perceptor())  # Crear la figura de Plotly con subplots

# Crear la figura de Plotly con subplots
fig = make_subplots(rows=1, cols=1)

# Definir el rango de valores de x
x_values = np.linspace(-10, 10, 100)  # Puedes ajustar el rango según tus necesidades

# Inicializar una lista para almacenar los datos de cada trazo
traces = []

colors = []
for i in range(len(ws)):
    colors.append('#%06X' % random.randint(0, 0xFFFFFF))

# Configurar los fotogramas de la animación
animation_frames = []

for i, w in enumerate(ws):
    y_values = (-w[0] - w[1] * x_values) / w[2]
    trace = go.Scatter(x=x_values, y=y_values, mode='lines', name=f'Recta {i + 1}', line=dict(color=colors[i]))
    traces.append(trace)

# Crear los fotogramas de animación
for i, trace in enumerate(traces):
    frame = go.Frame(data=trace)
    animation_frames.append(frame)
# Agregar los fotogramas de animación a la figura

fig = go.Figure(
    data=[traces[0], go.Scatter(x=[val[0] for val in values], y=[val[1] for val in values], mode='markers')],
    layout=go.Layout(
        xaxis=dict(range=[-10, 10], autorange=False),
        yaxis=dict(range=[-10, 10], autorange=False),
        title="Start Title",
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None])])]
    ),
    frames=animation_frames,

)

fig.show()
