from data_analysis_and_forecasting.mathematical_tools.mathematical_tool_interface import MathematicalToolInterface
from plotly.subplots import make_subplots
import plotly.graph_objects as go


class ExponentiallyWeightedMovingAverage(MathematicalToolInterface):

    def __init__(self):

        super().__init__()

    def _set_explanation(self):

        self.explanation = "The EWMA is a method used to calculate the trend or cycle components of a data series" \
            + " by smoothing out the noise of short-term fluctuations"

    def _set_figure(self):

        if self.input_data_info["dataUnit"] is None:
            y_axis_title = self.input_data_info["dataType"]
        else:
            y_axis_title = "{} ({})".format(
                self.input_data_info["dataType"],
                self.input_data_info["dataUnit"]
            )

        self.figure = make_subplots(
            rows=4,
            cols=1,
            shared_xaxes=True,
            x_title="<span style='font-size: 15px;' 'font-family: Helvetica, Calibri';><b>Date (Year)</b></span>",
            y_title="<span style='font-size: 15px;' 'font-family: Helvetica, Calibri';><b>" + y_axis_title + "</b></span>"
        )

        self.figure.append_trace(
            go.Scatter(
                x=self.input_data_info["dataArray"].index,
                y=self.input_data_info["dataArray"],
                name="Observed"
            ),
            row=1,
            col=1
        )

        self.figure.append_trace(
            go.Scatter(
                x=self.input_data_info["dataArray"].index,
                y=self.results["dataArrayEwma3monthsComponent"],
                name="3 months EWMA"
            ),
            row=2,
            col=1
        )

        self.figure.append_trace(
            go.Scatter(
                x=self.input_data_info["dataArray"].index,
                y=self.results["dataArrayEwma6monthsComponent"],
                name="6 months EWMA"
            ),
            row=3,
            col=1
        )

        self.figure.append_trace(
            go.Scatter(
                x=self.input_data_info["dataArray"].index,
                y=self.results["dataArrayEwma12monthsComponent"],
                name="12 months EWMA"
            ),
            row=4,
            col=1
        )

        self.figure.update_layout(
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

        data_array_ewma_3_months = self.input_data_info["dataArray"].ewm(span=3).mean()
        data_array_ewma_6_months = self.input_data_info["dataArray"].ewm(span=6).mean()
        data_array_ewma_12_months = self.input_data_info["dataArray"].ewm(span=12).mean()

        self.results["dataArrayEwma3monthsComponent"] = data_array_ewma_3_months
        self.results["dataArrayEwma6monthsComponent"] = data_array_ewma_6_months
        self.results["dataArrayEwma12monthsComponent"] = data_array_ewma_12_months
