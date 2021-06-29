from plotly.subplots import make_subplots
from statsmodels.tsa.seasonal import seasonal_decompose
import plotly.graph_objects as go


class ErrorTrendSeasonalityDecomposition:

    def __init__(self):

        self.error_trend_seasonality_decomposition = {
            "explanation": "The ETS Decomposition is a method used to calculate the error, trend and seasonal components of a data series",
            "components": {
                "dataArray": None,
                "dataArrayCycleComponent": None,
                "dataArraySeasonalComponent": None,
                "dataArrayTrendComponent": None
            },
            "dataset": None,
            "dataType": None,
            "dataUnit": None,
            "figure": None
        }

    def get_results(self):

        return self.error_trend_seasonality_decomposition

    def set(self, **kwargs):

        self.set_dataset(kwargs["dataset"])
        self.set_data_type(kwargs["dataType"])
        self.set_components(kwargs["dataArray"])
        self.set_figure()

    def set_components(self, data_array):

        result = seasonal_decompose(
            x=data_array,
            model="multiplicative"
        )

        self.error_trend_seasonality_decomposition["components"]["dataArray"] = data_array
        self.error_trend_seasonality_decomposition["components"]["dataArrayCycleComponent"] = result.resid
        self.error_trend_seasonality_decomposition["components"]["dataArraySeasonalComponent"] = result.seasonal
        self.error_trend_seasonality_decomposition["components"]["dataArrayTrendComponent"] = result.trend

    def set_dataset(self, dataset):

        self.error_trend_seasonality_decomposition["dataset"] = dataset

    def set_data_type(self, data_type):

        self.error_trend_seasonality_decomposition["dataType"] = data_type

    def set_figure(self):

        if self.error_trend_seasonality_decomposition["dataUnit"] is None:
            y_axis_title = self.error_trend_seasonality_decomposition["dataType"]
        else:
            y_axis_title = "{} ({})".format(
                self.error_trend_seasonality_decomposition["dataType"],
                self.error_trend_seasonality_decomposition["dataUnit"]
            )

        self.error_trend_seasonality_decomposition["figure"] = make_subplots(
            rows=4,
            cols=1,
            shared_xaxes=True,
            x_title="<span style='font-size: 15px'; 'font-family: Helvetica, Calibri';><b>Date (Year)</b></span>",
            y_title="<span style='font-size: 15px'; 'font-family: Helvetica, Calibri';><b>" + y_axis_title + "</b></span>"
        )

        self.error_trend_seasonality_decomposition["figure"].append_trace(
            go.Scatter(
                x=self.error_trend_seasonality_decomposition["components"]["dataArray"].index,
                y=self.error_trend_seasonality_decomposition["components"]["dataArray"],
                name="Observed"
            ),
            row=1,
            col=1
        )

        self.error_trend_seasonality_decomposition["figure"].append_trace(
            go.Scatter(
                x=self.error_trend_seasonality_decomposition["components"]["dataArray"].index,
                y=self.error_trend_seasonality_decomposition["components"]["dataArrayTrendComponent"],
                name="Trend component"
            ),
            row=2,
            col=1
        )

        self.error_trend_seasonality_decomposition["figure"].append_trace(
            go.Scatter(
                x=self.error_trend_seasonality_decomposition["components"]["dataArray"].index,
                y=self.error_trend_seasonality_decomposition["components"]["dataArraySeasonalComponent"],
                name="Seasonal component"
            ),
            row=3,
            col=1
        )

        self.error_trend_seasonality_decomposition["figure"].append_trace(
            go.Scatter(
                x=self.error_trend_seasonality_decomposition["components"]["dataArray"].index,
                y=self.error_trend_seasonality_decomposition["components"]["dataArrayCycleComponent"],
                name="Cycle component"
            ),
            row=4,
            col=1
        )

        self.error_trend_seasonality_decomposition["figure"].update_layout(
            title=dict(
                text="<span style='font-size: 22px'; 'font-family: Helvetica, Calibri';><b>{} X Datetime</b></span>".format(self.error_trend_seasonality_decomposition["dataType"]),
                y=0.94,
                x=0.5,
                xanchor='center',
                yanchor='top'
            ),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="center",
                x=0.5
            )
        )
