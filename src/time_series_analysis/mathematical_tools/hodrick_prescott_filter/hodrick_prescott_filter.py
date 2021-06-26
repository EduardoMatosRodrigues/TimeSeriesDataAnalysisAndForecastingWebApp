from plotly.subplots import make_subplots
from statsmodels.tsa.filters.hp_filter import hpfilter
import plotly.graph_objects as go


class HodrickPrescottFilter:

    def __init__(self):

        self.hodrick_prescott_filter = {
            "explanation": "The Hodrick-Prescott filter is a method used to calculate the trend and cycle components of a data series",
            "components": {
                "dataArray": None,
                "dataArrayCycleComponent": None,
                "dataArrayTrendComponent": None
            },
            "dataSet": None,
            "dataType": None,
            "dataUnit": None,
            "figure": None
        }

    def get_results(self):

        return self.hodrick_prescott_filter

    def set(self, **kwargs):

        self.set_dataset(kwargs["dataset"])
        self.set_data_type(kwargs["dataType"])
        self.set_data_unit(kwargs["dataUnit"])
        self.set_components(kwargs["dataArray"])
        self.set_figure()

    def set_components(self, data_array):

        x_cycle, x_trend = hpfilter(
            x=data_array,
            lamb=1600
        )

        self.hodrick_prescott_filter["components"]["dataArray"] = data_array
        self.hodrick_prescott_filter["components"]["dataArrayCycleComponent"] = x_cycle
        self.hodrick_prescott_filter["components"]["dataArrayTrendComponent"] = x_trend

    def set_dataset(self, dataset):

        self.hodrick_prescott_filter["dataset"] = dataset

    def set_data_type(self, data_type):

        self.hodrick_prescott_filter["dataType"] = data_type

    def set_data_unit(self, data_unit):

        self.hodrick_prescott_filter["dataUnit"] = data_unit

    def set_figure(self):

        if self.hodrick_prescott_filter["dataUnit"] is None:
            y_axis_title = self.hodrick_prescott_filter["dataType"]
        else:
            y_axis_title = "{} ({})".format(
                self.hodrick_prescott_filter["dataType"],
                self.hodrick_prescott_filter["dataUnit"]
            )

        self.hodrick_prescott_filter["figure"] = make_subplots(
            rows=3,
            cols=1,
            shared_xaxes=True,
            x_title="<span style='font-size: 15px'; 'font-family: Helvetica, Calibri';><b>Date (Year)</b></span>",
            y_title="<span style='font-size: 15px'; 'font-family: Helvetica, Calibri';><b>" + y_axis_title + "</b></span>"
        )

        self.hodrick_prescott_filter["figure"].append_trace(
            go.Scatter(
                x=self.hodrick_prescott_filter["components"]["dataArray"].index,
                y=self.hodrick_prescott_filter["components"]["dataArray"],
                name="Observed"
            ),
            row=1,
            col=1
        )

        self.hodrick_prescott_filter["figure"].append_trace(
            go.Scatter(
                x=self.hodrick_prescott_filter["components"]["dataArray"].index,
                y=self.hodrick_prescott_filter["components"]["dataArrayTrendComponent"],
                name="Trend component"
            ),
            row=2,
            col=1
        )

        self.hodrick_prescott_filter["figure"].append_trace(
            go.Scatter(
                x=self.hodrick_prescott_filter["components"]["dataArray"].index,
                y=self.hodrick_prescott_filter["components"]["dataArrayCycleComponent"],
                name="Cycle component"
            ),
            row=3,
            col=1
        )

        self.hodrick_prescott_filter["figure"].update_xaxes(dtick="M60", row=1, col=1)
        self.hodrick_prescott_filter["figure"].update_xaxes(dtick="M60", row=2, col=1)
        self.hodrick_prescott_filter["figure"].update_xaxes(dtick="M60", row=3, col=1)

        self.hodrick_prescott_filter["figure"].update_layout(
            height=395,
            title=dict(
                text="<span style='font-size: 22px'; 'font-family: Helvetica, Calibri';><b>{} X Datetime</b></span>".format(self.hodrick_prescott_filter["dataType"]),
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
