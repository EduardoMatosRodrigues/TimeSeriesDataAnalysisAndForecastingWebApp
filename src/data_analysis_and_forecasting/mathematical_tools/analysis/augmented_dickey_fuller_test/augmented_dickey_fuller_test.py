from data_analysis_and_forecasting.mathematical_tools.mathematical_tool_interface import MathematicalToolInterface
from plotly.subplots import make_subplots
from statsmodels.tsa.stattools import adfuller
import plotly.graph_objects as go


class AugmentedDickeyFullerTest(MathematicalToolInterface):

    def __init__(self):

        super().__init__()

    def _set_explanation(self):

        self.explanation = "The Augmented Dickey-Fuller Test is a unit root test to check whether a given time series is stationary or not"

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
                x=self.input_data_info["dataArray"].index,
                y=self.input_data_info["dataArray"],
            ),
            row=1,
            col=1
        )

        self.figure.add_annotation(
            x=0.02,
            y=0.93,
            xref="paper",
            yref="paper",
            text="<span style='font-size: 13px'; 'font-family: Helvetica, Calibri';><b>Test results</b></span><br>"
                 + "<span style='font-size: 11px'; 'font-family: Helvetica, Calibri';>{}</span>".format(self.results["testConclusion"]),
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
                text="<span style='font-size: 22px'; 'font-family: Helvetica, Calibri';><b>{} X Datetime</b></span>".format(self.input_data_info["dataType"]),
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

        augmented_dickey_fuller_test_results = adfuller(
            self.input_data_info["dataArray"],
            autolag='AIC'
        )

        self.results["pValue"] = round(augmented_dickey_fuller_test_results[1], 2)

        if self.results["pValue"] <= 0.05:
            self.results["testConclusion"] = \
                "<i>p</i> value = {} <= 0.05 (null hypothesis rejected)<br>".format(self.results["pValue"]) \
                + "<i>Conclusion</i>: The data is stationary"
        else:
            self.results["testConclusion"] = \
                "<i>p</i> value = {} > 0.05 (null hypothesis not rejected)<br>".format(self.results["pValue"]) \
                + "<i>Conclusion</i>: The data is non-stationary"
