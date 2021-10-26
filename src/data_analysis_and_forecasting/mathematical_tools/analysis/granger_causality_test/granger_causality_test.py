from data_analysis_and_forecasting.mathematical_tools.mathematical_tool_interface import MathematicalToolInterface
from plotly.subplots import make_subplots
from statsmodels.tsa.stattools import grangercausalitytests
import numpy as np
import pandas as pd
import plotly.graph_objects as go


class GrangerCausalityTest(MathematicalToolInterface):

    def __init__(self):

        super().__init__()

    def _set_input_data_info(self, **kwargs):

        self.input_data_info["dataArray1"] = kwargs["dataArray1"]
        self.input_data_info["dataArray2"] = kwargs["dataArray2"]
        self.input_data_info["dataSet"] = kwargs["dataSet"]
        self.input_data_info["dataType1"] = kwargs["dataType1"]
        self.input_data_info["dataType2"] = kwargs["dataType2"]
        self.input_data_info["dataUnit1"] = kwargs["dataUnit1"]
        self.input_data_info["dataUnit2"] = kwargs["dataUnit2"]

    def _set_explanation(self):

        self.explanation = "The Granger Causality Test is a statistical hypothesis test to check whether " \
                           + "the past (lagged) values of one time series have the ability to predict another"

    def _set_figure(self):

        self.figure = make_subplots(
            rows=len(self.results),
            cols=1,
            shared_xaxes=True,
            row_heights=[0.35, 0.65],
            x_title="<span style='font-size: 15px'; 'font-family: Helvetica, Calibri';><b>Date (Year)</b></span>",
            y_title="<span style='font-size: 15px'; 'font-family: Helvetica, Calibri';><b>Sample data</b></span>",
        )

        self.figure.append_trace(
            go.Scatter(
                x=self.input_data_info["dataArray1"].index,
                y=self.input_data_info["dataArray1"],
                name=self.input_data_info["dataType1"],
                legendgroup=self.input_data_info["dataType1"],
                line=dict(color='blue')
            ),
            row=1,
            col=1
        )

        self.figure.append_trace(
            go.Scatter(
                x=self.input_data_info["dataArray2"].index,
                y=self.input_data_info["dataArray2"],
                name=self.input_data_info["dataType2"],
                line=dict(color='red')
            ),
            row=1,
            col=1
        )

        self.figure.update_yaxes(
            range=[0, 100],
            dtick=25,
            row=1,
            col=1,
        )

        lag_number = len(list(self.results.keys()))

        self.figure.append_trace(
            go.Scatter(
                x=self.input_data_info["dataArray1"].index,
                y=self.input_data_info["dataArray1"],
                name=self.input_data_info["dataType1"],
                legendgroup=self.input_data_info["dataType1"],
                line=dict(color='blue'),
                showlegend=False
            ),
            row=2,
            col=1
        )

        self.figure.append_trace(
            go.Scatter(
                x=self.input_data_info["dataArray2"].index,
                y=self.input_data_info["dataArray2"].shift(lag_number),
                name="{} shifted by {}".format(
                    self.input_data_info["dataType2"],
                    lag_number
                ),
                line=dict(color='green')
            ),
            row=2,
            col=1
        )

        self.figure.update_yaxes(
            range=[0, 175],
            dtick=25,
            row=2,
            col=1,
        )

        self.figure.add_annotation(
            x=0.5,
            y=125,
            xref="x domain",
            yref="y2",
            text="<span style='font-size: 12px'; 'font-family: Helvetica, Calibri';><b>Test results for {} shifted by {}</b></span><br>".format(
                self.input_data_info["dataType2"].lower(),
                lag_number
            ) + "<span style='font-size: 10px'; 'font-family: Helvetica, Calibri'; 'line-height: 20pt';>{}</span>".format(self.results["lag{}".format(lag_number)]["testConclusion"]),
            align="left",
            bordercolor="black",
            borderwidth=1,
            borderpad=4,
            bgcolor="white",
            showarrow=False,
            font=dict(
                size=10
            )
        )

        self.figure.update_layout(
            height=395,
            title=dict(
                text="<span style='font-size: 22px'; 'font-family: Helvetica, Calibri';><b>{} and {} X Datetime</b></span>".format(
                    self.input_data_info["dataType1"],
                    self.input_data_info["dataType2"].lower()
                ),
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
                x=0.5,
                font=dict(
                    size=10
                ),
                tracegroupgap=0
            )
        )

    def _set_results(self):

        data = [self.input_data_info["dataArray1"], self.input_data_info["dataArray2"]]
        headers = [self.input_data_info["dataArray1"].name, self.input_data_info["dataArray2"].name]
        causality_dataframe = pd.concat(data, axis=1, keys=headers)

        maxlag = 2

        granger_causality_tests_results = grangercausalitytests(
            x=causality_dataframe[[self.input_data_info["dataArray1"].name, self.input_data_info["dataArray2"].name]],
            maxlag=maxlag,
            verbose=False
        )

        for lag_number in range(1, maxlag + 1):

            test_mean_pvalue = np.mean([
                round(granger_causality_tests_result[1], 2)
                for granger_causality_tests_result in granger_causality_tests_results[lag_number][0].values()
            ])

            if test_mean_pvalue <= 0.05:

                conclusion = \
                    "Mean <i>p</i> value of 4 tests = {:.2f} <= 0.05 (null hypothesis rejected)<br>".format(test_mean_pvalue) \
                    + "<i>Conclusion</i>: {} shifted by {} has the ability to predict {}".format(
                    self.input_data_info["dataType2"],
                    lag_number,
                    self.input_data_info["dataType1"].lower()
                )

            else:

                conclusion = \
                    "Mean <i>p</i> value of 4 tests = {:.2f} > 0.05 (null hypothesis not rejected)<br>".format(test_mean_pvalue) \
                    + "<i>Conclusion</i>: {} shifted by {} has no ability to predict {}".format(
                        self.input_data_info["dataType2"],
                        lag_number,
                        self.input_data_info["dataType1"].lower()
                    )

            self.results["lag{}".format(lag_number)] = {
                "testMeanPValue": test_mean_pvalue,
                "testConclusion": conclusion
            }

