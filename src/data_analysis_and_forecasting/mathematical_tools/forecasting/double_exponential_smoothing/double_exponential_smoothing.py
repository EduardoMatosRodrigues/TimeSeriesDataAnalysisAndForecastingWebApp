from data_analysis_and_forecasting.mathematical_tools.mathematical_tool_interface import MathematicalToolInterface
from plotly.subplots import make_subplots
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import numpy as np
import plotly.graph_objects as go


class DoubleExponentialSmoothing(MathematicalToolInterface):

    def __init__(self):

        super().__init__()

    def _set_explanation(self):

        self.explanation = "The Double Exponential Smoothing is a time series forecasting method for univariate data with trend but without seasonality"

    def _set_figure(self):

        if self.input_data_info["dataUnit"] is None:
            y_axis_title = self.input_data_info["dataType"]
        else:
            y_axis_title = "{} ({})".format(
                self.input_data_info["dataType"],
                self.input_data_info["dataUnit"]
            )

        self.figure = make_subplots(
            rows=1,
            cols=1,
            shared_xaxes=True,
            x_title="<span style='font-size: 15px'; 'font-family: Helvetica, Calibri';><b>Date (Year)</b></span>",
            y_title="<span style='font-size: 15px'; 'font-family: Helvetica, Calibri';><b>" + y_axis_title + "</b></span>"
        )

        self.figure.append_trace(
            go.Scatter(
                x=self.results["trainData"].index,
                y=self.results["trainData"],
                name="Train data"
            ),
            row=1,
            col=1
        )

        self.figure.append_trace(
            go.Scatter(
                x=self.results["testData"].index,
                y=self.results["testData"],
                name="Test data"
            ),
            row=1,
            col=1
        )

        self.figure.append_trace(
            go.Scatter(
                x=self.results["fittedData"].index,
                y=self.results["fittedData"],
                name="Fitted data"
            ),
            row=1,
            col=1
        )

        self.figure.append_trace(
            go.Scatter(
                x=self.results["forecastData"].index,
                y=self.results["forecastData"],
                name="Forecast data"
            ),
            row=1,
            col=1
        )

        self.figure.add_annotation(
            x=0.02,
            y=0.92,
            xref="paper",
            yref="paper",
            text="<span style='font-size: 13px'; 'font-family: Helvetica, Calibri';><b>Forecast evaluation</b></span><br>"
                 + "<span style='font-size: 11px'; 'font-family: Helvetica, Calibri';>RMSE: {}</span>".format(round(self.results["forecastEvaluation"], 2)),
            align="left",
            bordercolor="black",
            borderwidth=1,
            borderpad=7.5,
            bgcolor="white",
            showarrow=False,
        )

        self.figure.update_layout(
            height=395,
            title=dict(
                text="<span style='font-size: 22px'; 'font-family: Helvetica, Calibri';><b>{} X Date</b></span>".format(self.input_data_info["dataType"]),
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

    def _set_results(self):

        train_data = self.input_data_info["dataArray"].iloc[:int(0.8 * len(self.input_data_info["dataArray"]))]
        test_data = self.input_data_info["dataArray"].iloc[int(0.8 * len(self.input_data_info["dataArray"])) - 1:]

        model = ExponentialSmoothing(
            endog=train_data,
            trend="mul"
        )
        fitted_model = model.fit()

        fitted_data = fitted_model.fittedvalues.shift(-1)
        forecast_data = fitted_model.forecast(len(test_data))

        forecast_rmse = mean_squared_error(
            y_true=test_data,
            y_pred=forecast_data,
            squared=False
        )

        self.results["trainData"] = train_data
        self.results["testData"] = test_data
        self.results["fittedData"] = fitted_data
        self.results["forecastData"] = forecast_data
        self.results["forecastEvaluation"] = forecast_rmse
