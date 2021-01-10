from plotly.subplots import make_subplots
from categories import get_cmap
import plotly.graph_objects as go
import numpy as np


class CodePlot():
    def __init__(self, code_a, code_b, threshold = 0.8):
        self._fig = go.Figure()
        self._code_a = code_a
        self._code_b = code_b
        self._threshold = threshold
        self.__create() # Create the plot for code_a and code_b

    @property
    def fig(self):
        return self._fig

    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, t):
        self._threshold = t # Set new threshold for similarity overlay

        # Update cmap of overlay trace with new threshold
        self._fig.data[2].update(colorscale=self.__overlay_cmap())


    def __overlay_cmap(self):
        return [[0, "rgb(255, 255, 255)"],[self._threshold, "rgb(255, 255, 255)"],
               [self._threshold, "rgb(255, 0, 0)"], [1, "rgb(255, 0, 0)"]]

    def __get_traces(self):
        filename_a = self._code_a.name
        filename_b = self._code_b.name
        data_a = self._code_a.get_ctg_array()
        data_a_sim = self._code_a.get_sim_array()
        data_b = self._code_b.get_ctg_array()
        labels_a = self._code_a.get_clnstr_array()
        labels_b = self._code_b.get_clnstr_array()

        # code_a heatmap
        trace_a = go.Heatmap(
            z=data_a, text=labels_a, name=filename_a, showscale=False, colorscale=get_cmap(),
            hovertemplate='Row: %{y}<br>Column: %{x}<br>String: \'%{text}\'<extra></extra>')

        # code_b heatmap
        trace_b = go.Heatmap(
            z=data_b, text=labels_b, name=filename_b, showscale=False, colorscale=get_cmap(),
            hovertemplate='Row: %{y}<br>Column: %{x}<br>String: \'%{text}\'<extra></extra>')

        # similarity heatmap, serves as filteror the heatmap of code_a
        trace_a_sim = go.Heatmap(z=data_a_sim, visible=True, showscale=False, zmax=1.0, zmin=0.0,
                        colorscale=self.__overlay_cmap(), opacity=0.8, hovertemplate='Similarity: %{z}\'<extra></extra>')

        return[trace_a, trace_b, trace_a_sim]


    def __make_subplots(self):
        traces = self.__get_traces()

        # Create subplots to show both codes side by side
        self._fig = make_subplots(rows=1, cols=2, subplot_titles=[self._code_a.name, self._code_b.name])

        # Append all heatmaps to according subplots
        self._fig.append_trace(traces[0], 1, 1)
        self._fig.append_trace(traces[1], 1, 2)
        self._fig.append_trace(traces[2], 1, 1)


    def __update_layout(self):
        # Change the layout of heatmaps to fit code representation
        self._fig.update_yaxes(title_text="Line", autorange="reversed", 
                            mirror=True, ticks='outside', showline=True, linecolor='black')
        self._fig.update_xaxes(title_text="Column", 
                            mirror=True, ticks='outside', showline=True, linecolor='black')
        self._fig.update_layout(title_text="Vizualized Result", title_font_size=33)

        marginTop = 100
        marginBottom = 10
        plotHeight = max([len(self._code_a), len(self._code_b)]) * 8 + marginTop + marginBottom

        if plotHeight < 600:
            plotHeight = 600

        self._fig.update_layout(height=plotHeight, margin=dict(t=marginTop, b=marginBottom, l=0), 
                                width=900, hovermode='x')


    def __create(self):
        self.__make_subplots()
        self.__update_layout()