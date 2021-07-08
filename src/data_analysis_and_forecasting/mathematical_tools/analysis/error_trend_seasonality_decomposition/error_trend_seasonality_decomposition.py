from data_analysis_and_forecasting.mathematical_tools.mathematical_tool_interface import MathematicalToolInterface
from plotly.subplots import make_subplots
from statsmodels.tsa.seasonal import seasonal_decompose
import plotly.graph_objects as go


class ErrorTrendSeasonalityDecomposition(MathematicalToolInterface):

    def __init__(self):

        super().__init__()

    def _set_explanation(self):

        self.explanation = "The ETS Decomposition is a method used to calculate the error, trend and seasonal components of a data series"

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
            x_title="<span style='font-size: 15px'; 'font-family: Helvetica, Calibri';><b>Date (Year)</b></span>",
            y_title="<span style='font-size: 15px'; 'font-family: Helvetica, Calibri';><b>" + y_axis_title + "</b></span>"
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
                y=self.results["dataArrayTrendComponent"],
                name="Trend component"
            ),
            row=2,
            col=1
        )

        self.figure.append_trace(
            go.Scatter(
                x=self.input_data_info["dataArray"].index,
                y=self.results["dataArraySeasonalComponent"],
                name="Seasonal component"
            ),
            row=3,
            col=1
        )

        self.figure.append_trace(
            go.Scatter(
                x=self.input_data_info["dataArray"].index,
                y=self.results["dataArrayCycleComponent"],
                name="Cycle component"
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

        result = seasonal_decompose(
            x=self.input_data_info["dataArray"],
            model="multiplicative"
        )

        self.results["dataArrayCycleComponent"] = result.resid
        self.results["dataArraySeasonalComponent"] = result.seasonal
        self.results["dataArrayTrendComponent"] = result.trend
