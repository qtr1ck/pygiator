# Example - Draw a plot using plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np


def draw_plot(code_a, code_b):
    fig = go.Figure()

    data_a = code_a.get_ctg_array()
    data_b = code_b.get_ctg_array()

    labels_a = code_a.get_clnstr_array()
    labels_b = code_b.get_clnstr_array()

    trace_a = go.Heatmap(
        z=data_a, text=labels_a, name="Code A", showscale=False,
        hovertemplate='Row: %{y}<br>Column: %{x}<br>String: \'%{text}\'<extra></extra>')

    trace_b = go.Heatmap(
        z=data_b, text=labels_b, name="Code B", showscale=False,
        hovertemplate='Row: %{y}<br>Column: %{x}<br>String: \'%{text}\'<extra></extra>')

    fig = make_subplots(rows=1, cols=2)

    fig.append_trace(trace_a, 1, 1)
    fig.append_trace(trace_b, 1, 2)

    data_a_sim = code_a.get_sim_array()
    # Add traces for slider steps
    for step in np.arange(0, 1, 0.1):
        trace_a_sim = go.Heatmap(z=data_a_sim, visible=False, showscale=False,
        hoverinfo='skip', colorscale='Bluered', opacity=step)
        fig.append_trace(trace_a_sim, 1, 1)


    fig.update_yaxes(title_text="Row", autorange="reversed", row=1, col=1)
    fig.update_yaxes(title_text="Row", autorange="reversed", row=1, col=2)
    fig.update_xaxes(title_text="Column", row=1, col=1)
    fig.update_xaxes(title_text="Column", row=1, col=2)


    # Create and add slider
    steps = []


    for i in range(len(fig.data)-2):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(fig.data)}],
            label=(i+1)/10,  # layout attribute
        )
        step["args"][0]["visible"][0] = True  # Toggle 1st trace to "visible"
        step["args"][0]["visible"][1] = True  # Toggle 2nd trace to "visible"
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps.append(step)


    sliders = [dict(
        active=10,
        currentvalue={"prefix": "Opacity: "},
        pad={"t": 50},
        steps=steps
    )]

    fig.update_layout(sliders=sliders)

    #fig.show()
    return fig