from plotly.subplots import make_subplots
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import numpy as np
import plotly.graph_objects as go


class DoubleExponentialSmoothing:

    def __init__(self):

        self.double_exponential_smoothing = {
            "explanation": "The Double Exponential Smoothing is a time series forecasting method for univariate data with trend but without seasonality",
            "components": {
                "trainData": None,
                "testData": None,
                "fittedData": None,
                "forecastData": None,
            },
            "dataSet": None,
            "dataType": None,
            "dataUnit": None,
            "forecastEvaluation": None,
            "figure": None
        }

    def get_results(self):

        return self.double_exponential_smoothing

    def set(self, **kwargs):

        self.set_dataset(kwargs["dataset"])
        self.set_data_type(kwargs["dataType"])
        self.set_components(kwargs["dataArray"])
        self.set_forecast_evaluation()
        self.set_figure()

    def set_components(self, data_array):

        train_data = data_array.iloc[:int(0.8 * len(data_array))]
        test_data = data_array.iloc[int(0.8 * len(data_array)) - 1:]

        model = ExponentialSmoothing(
            train_data,
            trend="mul"
        )
        fitted_model = model.fit()

        self.double_exponential_smoothing["components"]["trainData"] = train_data
        self.double_exponential_smoothing["components"]["testData"] = test_data
        self.double_exponential_smoothing["components"]["fittedData"] = fitted_model.fittedvalues.shift(-1)
        self.double_exponential_smoothing["components"]["forecastData"] = fitted_model.forecast(len(test_data))

    def set_dataset(self, dataset):

        self.double_exponential_smoothing["dataset"] = dataset

    def set_data_type(self, data_type):

        self.double_exponential_smoothing["dataType"] = data_type

    def set_figure(self):

        if self.double_exponential_smoothing["dataUnit"] is None:
            y_axis_title = self.double_exponential_smoothing["dataType"]
        else:
            y_axis_title = "{} ({})".format(
                self.double_exponential_smoothing["dataType"],
                self.double_exponential_smoothing["dataUnit"]
            )

        self.double_exponential_smoothing["figure"] = make_subplots(
            rows=1,
            cols=1,
            shared_xaxes=True,
            x_title="<span style='font-size: 15px'; 'font-family: Helvetica, Calibri';><b>Date (Year)</b></span>",
            y_title="<span style='font-size: 15px'; 'font-family: Helvetica, Calibri';><b>" + y_axis_title + "</b></span>"
        )

        self.double_exponential_smoothing["figure"].append_trace(
            go.Scatter(
                x=self.double_exponential_smoothing["components"]["trainData"].index,
                y=self.double_exponential_smoothing["components"]["trainData"],
                name="Train data"
            ),
            row=1,
            col=1
        )

        self.double_exponential_smoothing["figure"].append_trace(
            go.Scatter(
                x=self.double_exponential_smoothing["components"]["testData"].index,
                y=self.double_exponential_smoothing["components"]["testData"],
                name="Test data"
            ),
            row=1,
            col=1
        )

        self.double_exponential_smoothing["figure"].append_trace(
            go.Scatter(
                x=self.double_exponential_smoothing["components"]["fittedData"].index,
                y=self.double_exponential_smoothing["components"]["fittedData"],
                name="Fitted data"
            ),
            row=1,
            col=1
        )

        self.double_exponential_smoothing["figure"].append_trace(
            go.Scatter(
                x=self.double_exponential_smoothing["components"]["forecastData"].index,
                y=self.double_exponential_smoothing["components"]["forecastData"],
                name="Forecast data"
            ),
            row=1,
            col=1
        )

        self.double_exponential_smoothing["figure"].add_annotation(
            x=0.02,
            y=0.92,
            xref="paper",
            yref="paper",
            text="<span style='font-size: 13px'; 'font-family: Helvetica, Calibri';><b>Forecast evaluation</b></span><br>"
                 + "<span style='font-size: 11px'; 'font-family: Helvetica, Calibri';>RMSE: {}</span>".format(round(self.double_exponential_smoothing["forecastEvaluation"], 2)),
            align="left",
            bordercolor="black",
            borderwidth=1,
            borderpad=7.5,
            bgcolor="white",
            showarrow=False,
        )

        self.double_exponential_smoothing["figure"].update_layout(
            height=395,
            title=dict(
                text="<span style='font-size: 22px'; 'font-family: Helvetica, Calibri';><b>{} X Datetime</b></span>".format(self.double_exponential_smoothing["dataType"]),
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

    def set_forecast_evaluation(self):

        mse = mean_squared_error(
            self.double_exponential_smoothing["components"]["testData"],
            self.double_exponential_smoothing["components"]["forecastData"]
        )
        rmse = np.sqrt(mse)

        self.double_exponential_smoothing["forecastEvaluation"] = rmse