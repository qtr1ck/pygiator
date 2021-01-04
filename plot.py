# Example - Draw a plot using plotly
from plotly.subplots import make_subplots
from categories import get_cmap
import plotly.graph_objects as go
import numpy as np


class sim_marker():
    
    def __init__(self, threshold = 0.8):
        self.cmap = [0, "rgb(255, 255, 255)"],[threshold, "rgb(255, 255, 255)"], [threshold, "rgb(255, 0, 0)"], [1, "rgb(255, 0, 0)"]

    def set_threshold(self, threshold):
        self.cmap = [0, "rgb(255, 255, 255)"],[threshold, "rgb(255, 255, 255)"], [threshold, "rgb(255, 0, 0)"], [1, "rgb(255, 0, 0)"]

    def get_map(self):
        return self.cmap



def draw_plot(code_a, code_b, sim_marker, filename_A = "Code A", filename_B = "Code B"):
    fig = go.Figure()

    data_a = code_a.get_ctg_array()
    data_b = code_b.get_ctg_array()

    labels_a = code_a.get_clnstr_array()
    labels_b = code_b.get_clnstr_array()

    trace_a = go.Heatmap(
        z=data_a, text=labels_a, name=filename_A, showscale=False, colorscale=get_cmap(),
        hovertemplate='Row: %{y}<br>Column: %{x}<br>String: \'%{text}\'<extra></extra>')

    trace_b = go.Heatmap(
        z=data_b, text=labels_b, name=filename_B, showscale=False, colorscale=get_cmap(),
        hovertemplate='Row: %{y}<br>Column: %{x}<br>String: \'%{text}\'<extra></extra>')

    fig = make_subplots(rows=1, cols=2)

    fig.append_trace(trace_a, 1, 1)
    fig.append_trace(trace_b, 1, 2)

    data_a_sim = code_a.get_sim_array()

    s = sim_marker

    trace_a_sim = go.Heatmap(z=data_a_sim, name=filename_A, visible=True, showscale=False, colorscale=s.get_map(),
                            opacity=0.8,
                             hovertemplate='Similarity: %{z}\'<extra></extra>') 
    fig.append_trace(trace_a_sim, 1, 1)

    fig.update_yaxes(title_text="Row", autorange="reversed", row=1, col=1)
    fig.update_yaxes(title_text="Row", autorange="reversed", row=1, col=2)
    fig.update_xaxes(title_text="Column", row=1, col=1)
    fig.update_xaxes(title_text="Column", row=1, col=2)

    return fig