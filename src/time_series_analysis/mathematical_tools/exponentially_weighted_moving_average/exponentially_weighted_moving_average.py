from plotly.subplots import make_subplots
import plotly.graph_objects as go


class ExponentiallyWeightedMovingAverage:

    def __init__(self):

        self.exponentially_weighted_moving_average = {
            "explanation": "The EWMA is a method used to calculate the trend or cycle components of a data series by smoothing out the noise of short-term fluctuations",
            "components": {
                "dataArray": None,
                "dataArrayEwma3monthsComponent": None,
                "dataArrayEwma6monthsComponent": None,
                "dataArrayEwma12monthsComponent": None
            },
            "dataset": None,
            "dataType": None,
            "dataUnit": None,
            "figure": None
        }

    def get_results(self):

        return self.exponentially_weighted_moving_average

    def set(self, **kwargs):

        self.set_dataset(kwargs["dataset"])
        self.set_data_type(kwargs["dataType"])
        self.set_components(kwargs["dataArray"])
        self.set_figure()

    def set_components(self, data_array):

        data_array_ewma_3_months = data_array.ewm(span=3).mean()
        data_array_ewma_6_months = data_array.ewm(span=6).mean()
        data_array_ewma_12_months = data_array.ewm(span=12).mean()

        self.exponentially_weighted_moving_average["components"]["dataArray"] = data_array
        self.exponentially_weighted_moving_average["components"]["dataArrayEwma3monthsComponent"] = data_array_ewma_3_months
        self.exponentially_weighted_moving_average["components"]["dataArrayEwma6monthsComponent"] = data_array_ewma_6_months
        self.exponentially_weighted_moving_average["components"]["dataArrayEwma12monthsComponent"] = data_array_ewma_12_months

    def set_dataset(self, dataset):

        self.exponentially_weighted_moving_average["dataset"] = dataset

    def set_data_type(self, data_type):

        self.exponentially_weighted_moving_average["dataType"] = data_type

    def set_figure(self):

        if self.exponentially_weighted_moving_average["dataUnit"] is None:
            y_axis_title = self.exponentially_weighted_moving_average["dataType"]
        else:
            y_axis_title = "{} ({})".format(
                self.exponentially_weighted_moving_average["dataType"],
                self.exponentially_weighted_moving_average["dataUnit"]
            )

        self.exponentially_weighted_moving_average["figure"] = make_subplots(
            rows=4,
            cols=1,
            shared_xaxes=True,
            x_title="<span style='font-size: 15px;' 'font-family: Helvetica, Calibri';><b>Date (Year)</b></span>",
            y_title="<span style='font-size: 15px;' 'font-family: Helvetica, Calibri';><b>" + y_axis_title + "</b></span>"
        )

        self.exponentially_weighted_moving_average["figure"].append_trace(
            go.Scatter(
                x=self.exponentially_weighted_moving_average["components"]["dataArray"].index,
                y=self.exponentially_weighted_moving_average["components"]["dataArray"],
                name="Observed"
            ),
            row=1,
            col=1
        )

        self.exponentially_weighted_moving_average["figure"].append_trace(
            go.Scatter(
                x=self.exponentially_weighted_moving_average["components"]["dataArray"].index,
                y=self.exponentially_weighted_moving_average["components"]["dataArrayEwma3monthsComponent"],
                name="3 months EWMA"
            ),
            row=2,
            col=1
        )

        self.exponentially_weighted_moving_average["figure"].append_trace(
            go.Scatter(
                x=self.exponentially_weighted_moving_average["components"]["dataArray"].index,
                y=self.exponentially_weighted_moving_average["components"]["dataArrayEwma6monthsComponent"],
                name="6 months EWMA"
            ),
            row=3,
            col=1
        )

        self.exponentially_weighted_moving_average["figure"].append_trace(
            go.Scatter(
                x=self.exponentially_weighted_moving_average["components"]["dataArray"].index,
                y=self.exponentially_weighted_moving_average["components"]["dataArrayEwma12monthsComponent"],
                name="12 months EWMA"
            ),
            row=4,
            col=1
        )

        self.exponentially_weighted_moving_average["figure"].update_layout(
            title=dict(
                text="<span style='font-size: 22px'; 'font-family: Helvetica, Calibri';><b>{} X Datetime</b></span>".format(self.exponentially_weighted_moving_average["dataType"]),
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
