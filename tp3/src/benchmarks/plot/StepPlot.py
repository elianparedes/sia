import os

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from src.classes.perceptron.Step import Step
from src.utils.Function import *
from Config import Config

DATA_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, os.path.pardir,
                           "Data", "TP3-ej2-conjunto.csv")

LEARNING_RATE = 0.1
EPOCHS = 500


def step_error_plot(training_set, training_expected, error_title, animation_title, speed, frame_duration):
    # Error plot
    perceptron = Step(3, LEARNING_RATE)
    w_min, iterations, previous_weights, previous_errors, _ = perceptron.train(training_set, training_expected, training_set, training_expected, batch_amount=1, epoch=EPOCHS, epsilon=0)
    x = [i for i in range(iterations)]
    data = {'Epochs': x, 'Error': previous_errors}
    df = pd.DataFrame(data)
    fig = px.line(df, x="Epochs", y="Error", title=error_title)
    fig.show()

    # Linear separation animated plot (https://plotly.com/python/animations/)
    # Layout
    fig_dict = {
        "data": [],
        "layout": {},
        "frames": []
    }

    fig_dict["layout"]["title"] = animation_title
    fig_dict["layout"]["xaxis"] = {"range": [-2, 2], "title": "x"}
    fig_dict["layout"]["yaxis"] = {"range": [-2, 2], "title": "y"}
    fig_dict["layout"]["hovermode"] = "closest"
    fig_dict["layout"]["updatemenus"] = [
        {
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": speed, "redraw": True},
                                    "fromcurrent": True, "transition": {"duration": frame_duration,
                                                                        "easing": "quadratic-in-out"}}],
                    "label": "Play",
                    "method": "animate"
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": True},
                                      "mode": "immediate",
                                      "transition": {"duration": 0}}],
                    "label": "Pause",
                    "method": "animate"
                }
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 87},
            "showactive": False,
            "type": "buttons",
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top",
        }
    ]

    sliders_dict = {
        "active": 0,
        "yanchor": "top",
        "xanchor": "left",
        "currentvalue": {
            "font": {"size": 20},
            "prefix": "Epoch:",
            "visible": True,
            "xanchor": "right"
        },
        "transition": {"duration": frame_duration, "easing": "cubic-in-out"},
        "pad": {"b": 10, "t": 50},
        "len": 0.9,
        "x": 0.1,
        "y": 0,
        "steps": []
    }

    # append the line to the plot
    weight = previous_weights[0]
    y1 = (-weight[0] - (-2) * weight[1]) / weight[2]
    y2 = (-weight[0] - 8 * weight[1]) / weight[2]
    fig_dict["data"].append(go.Scatter(x=[-2, 8], y=[y1, y2], showlegend=False))

    # append scatter points to the plot
    first_class_x = []
    first_class_y = []
    second_class_x = []
    second_class_y = []
    for i in range(0, len(training_set)):
        if training_expected[i] == 1:
            first_class_x.append(training_set[i][1])
            first_class_y.append(training_set[i][2])
        else:
            second_class_x.append(training_set[i][1])
            second_class_y.append(training_set[i][2])

    fig_dict["data"].append(go.Scatter(x=first_class_x, y=first_class_y, mode='markers', showlegend=False))
    fig_dict["data"].append(go.Scatter(x=second_class_x, y=second_class_y, mode='markers', showlegend=False))

    # make frames (lines)
    for i in range(1, len(previous_weights)):
        frame = {"data": [], "name": str(i)}

        weight = previous_weights[i]
        y1 = (-weight[0] - (-2) * weight[1]) / weight[2]
        y2 = (-weight[0] - 8 * weight[1]) / weight[2]

        frame["data"].append(go.Scatter(x=[-2, 8], y=[y1, y2]))
        fig_dict["frames"].append(frame)
        slider_step = {"args": [
            [i],
            {"frame": {"duration": frame_duration, "redraw": True},
             "mode": "immediate",
             "transition": {"duration": frame_duration}}
        ],
            "label": i,
            "method": "animate"}
        sliders_dict["steps"].append(slider_step)

    fig_dict["layout"]["sliders"] = [sliders_dict]
    fig = go.Figure(fig_dict)

    fig.update_traces(marker_size=10)
    fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='black')
    fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='black')
    fig.show()


def and_step_plot(training_set, training_expected, speed, frame_duration):
    step_error_plot(training_set, training_expected, 'Error value by Epochs (AND function)',
                    'Linear separation (AND function)', speed, frame_duration)


def xor_step_plot(training_set, training_expected, speed, frame_duration):
    # XOR function (cannot be solved with a simple perceptron)
    step_error_plot(training_set, training_expected, 'Error value by Epochs (XOR function)',
                    'Linear separation (XOR function)', speed, frame_duration)
