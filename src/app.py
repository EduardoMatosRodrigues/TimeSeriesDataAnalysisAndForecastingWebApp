from dash.dependencies import Input, Output
from datasets.datasets import Datasets
from layout.layout import AppLayout
from time_series_analysis.time_series_analysis import TimeSeriesAnalysis
import dash

app_version = "1.00"

datasets = Datasets()
datasets.set()

time_series_analysis = TimeSeriesAnalysis(datasets)
time_series_analysis.set_results()

app = dash.Dash()

app_layout = AppLayout()

app.layout = app_layout.get(app_version)


@app.callback(
    Output('mathematical-tool-results-figure', 'figure'),
    Output('dataset-explanation', 'children'),
    Output('mathematical-tool-explanation', 'children'),
    [Input('mathematical-tool-dropdown', 'value')])
def update_output(value):

    return time_series_analysis.get_results()[value]["figure"], \
           datasets.get()[time_series_analysis.get_results()[value]["dataset"]]["explanation"], \
           time_series_analysis.get_results()[value]["explanation"]


if __name__ == '__main__':

    app.run_server(
        host="0.0.0.0",
        port=80
    )
