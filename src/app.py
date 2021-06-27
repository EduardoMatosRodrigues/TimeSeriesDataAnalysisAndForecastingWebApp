from dash.dependencies import Input, Output
from datasets.datasets import Datasets
from layout.layout import AppLayout
from data_analysis_and_forecasting.data_analysis_and_forecasting import DataAnalysisAndForecasting
import dash

app_version = "1.00"

datasets = Datasets()
datasets.set()

data_analysis_and_forecasting = DataAnalysisAndForecasting(datasets)
data_analysis_and_forecasting.set_results()

app = dash.Dash()

app_layout = AppLayout()

app.layout = app_layout.get(app_version)


@app.callback(
    Output('mathematical-tool-dropdown', 'options'),
    Output('mathematical-tool-dropdown', 'value'),
    Input('app-card-internal-left-tabs', 'value')
)
def render_content(tab):

    if tab == 'tab-analysis':

        dropdown_options = [
            {'label': 'Hodrick-Prescott Filter', 'value': 'hodrickPrescottFilter'},
            {'label': 'ETS Decomposition', 'value': 'errorTrendSeasonalityDecomposition'},
            {'label': 'Simple Moving Average', 'value': 'simpleMovingAverage'},
            {'label': 'Exponentially Weighed Moving Average', 'value': 'exponentiallyWeightedMovingAverage'},
        ]
        dropdown_value = 'hodrickPrescottFilter'

        return dropdown_options, dropdown_value

    elif tab == 'tab-forecasting':

        dropdown_options = [
            {'label': 'Simple Exponential Smoothing', 'value': 'simpleExponentialSmoothing'},
            {'label': 'Double Exponential Smoothing (Holt Method)', 'value': 'doubleExponentialSmoothing'},
            {'label': 'Triple Exponential Smoothing (Holt-Winters Method)', 'value': 'tripleExponentialSmoothing'}
        ]
        dropdown_value = 'simpleExponentialSmoothing'

        return dropdown_options, dropdown_value


@app.callback(
    Output('mathematical-tool-results-figure', 'figure'),
    Output('dataset-explanation', 'children'),
    Output('mathematical-tool-explanation', 'children'),
    Input('mathematical-tool-dropdown', 'value')
)
def update_output(value):

    return data_analysis_and_forecasting.get_results()[value]["figure"], \
           datasets.get()[data_analysis_and_forecasting.get_results()[value]["dataset"]]["explanation"], \
           data_analysis_and_forecasting.get_results()[value]["explanation"]


if __name__ == '__main__':

    app.run_server(
        host="0.0.0.0",
        port=80
    )
