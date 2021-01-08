from plotly.subplots import make_subplots
from categories import get_cmap
import plotly.graph_objects as go
import numpy as np


# Class object to make change of similarity overlay in plot possible
class sim_marker():
    
    def __init__(self, threshold = 0.8):
        self.cmap = [0, "rgb(255, 255, 255)"],[threshold, "rgb(255, 255, 255)"], [threshold, "rgb(255, 0, 0)"], [1, "rgb(255, 0, 0)"]

    def set_threshold(self, threshold):
        self.cmap = [0, "rgb(255, 255, 255)"],[threshold, "rgb(255, 255, 255)"], [threshold, "rgb(255, 0, 0)"], [1, "rgb(255, 0, 0)"]

    def get_map(self):
        return self.cmap


# Draw code representation as plots
def draw_plot(code_a, code_b, sim_marker):
    fig = go.Figure()

    # stores required data from code_a and code_b into variables for convenience
    filename_a = code_a.name
    filename_b = code_b.name
    data_a = code_a.get_ctg_array()
    data_b = code_b.get_ctg_array()
    labels_a = code_a.get_clnstr_array()
    labels_b = code_b.get_clnstr_array()

    # code_a heatmap
    trace_a = go.Heatmap(
        z=data_a, text=labels_a, name=filename_a, showscale=False, colorscale=get_cmap(),
        hovertemplate='Row: %{y}<br>Column: %{x}<br>String: \'%{text}\'<extra></extra>')

    # code_b heatmap
    trace_b = go.Heatmap(
        z=data_b, text=labels_b, name=filename_b, showscale=False, colorscale=get_cmap(),
        hovertemplate='Row: %{y}<br>Column: %{x}<br>String: \'%{text}\'<extra></extra>')

    data_a_sim = code_a.get_sim_array()
    s = sim_marker  # color map for similarity
    # similarity heatmap, serves as filteror the heatmap of code_a
    trace_a_sim = go.Heatmap(z=data_a_sim, name=filename_a, visible=True, showscale=False, colorscale=s.get_map(),
                            opacity=0.8, hovertemplate='Similarity: %{z}\'<extra></extra>')
    

    # Create subplots to show both codes side by side
    fig = make_subplots(rows=1, cols=2, subplot_titles=[filename_a, filename_b])

    # Append all heatmaps to according subplots
    fig.append_trace(trace_a, 1, 1)
    fig.append_trace(trace_b, 1, 2)
    fig.append_trace(trace_a_sim, 1, 1)

    # Change the layout of heatmaps to fit code representation
    fig.update_yaxes(title_text="Line", autorange="reversed", 
                        mirror=True, ticks='outside', showline=True, linecolor='black')
    fig.update_xaxes(title_text="Block", 
                        mirror=True, ticks='outside', showline=True, linecolor='black')
    fig.update_layout(title_text="Vizualized Result", title_font_size=33)

    marginTop = 100
    marginBottom = 10
    plotHeight = max([len(code_a), len(code_b)]) * 8 + marginTop + marginBottom

    if plotHeight < 600:
        plotHeight = 600

    fig.update_layout(height=plotHeight, margin=dict(t=marginTop, b=marginBottom, l=0), width=900)

    return fig