from time_series_analysis.mathematical_tools.error_trend_seasonality_decomposition.error_trend_seasonality_decomposition import ErrorTrendSeasonalityDecomposition
from time_series_analysis.mathematical_tools.exponentially_weighted_moving_average.exponentially_weighted_moving_average import ExponentiallyWeightedMovingAverage
from time_series_analysis.mathematical_tools.hodrick_prescott_filter.hodrick_prescott_filter import HodrickPrescottFilter
from time_series_analysis.mathematical_tools.simple_moving_average.simple_moving_average import SimpleMovingAverage


class TimeSeriesAnalysis:

    def __init__(self, datasets):

        self.results = {}

        self.datasets = datasets.get()

    def get_results(self):

        return self.results

    def set_results(self):

        self.set_hodrick_prescott_filter()
        self.set_error_trend_seasonality_decomposition()
        self.set_simple_moving_average()
        self.set_exponentially_weighted_moving_average()

    def set_hodrick_prescott_filter(self):

        hodrick_prescott_filter = HodrickPrescottFilter()
        hodrick_prescott_filter.set(
            dataArray=self.datasets["usMacroeconomic"]["pandasDataframe"]["realgdp"],
            dataset="usMacroeconomic",
            dataType="Real GDP",
            dataUnit="Billions of US$"
        )

        self.results["hodrickPrescottFilter"] = hodrick_prescott_filter.get_results()

    def set_error_trend_seasonality_decomposition(self):

        error_trend_seasonality_decomposition = ErrorTrendSeasonalityDecomposition()
        error_trend_seasonality_decomposition.set(
            dataArray=self.datasets["internationalAirlinePassengers"]["pandasDataframe"]["Thousands of Passengers"],
            dataset="internationalAirlinePassengers",
            dataType="Passengers"
        )

        self.results["errorTrendSeasonalityDecomposition"] = error_trend_seasonality_decomposition.get_results()

    def set_simple_moving_average(self):

        simple_moving_average = SimpleMovingAverage()
        simple_moving_average.set(
            dataArray=self.datasets["internationalAirlinePassengers"]["pandasDataframe"]["Thousands of Passengers"],
            dataset="internationalAirlinePassengers",
            dataType="Passengers"
        )

        self.results["simpleMovingAverage"] = simple_moving_average.get_results()

    def set_exponentially_weighted_moving_average(self):

        exponentially_weighted_moving_average = ExponentiallyWeightedMovingAverage()
        exponentially_weighted_moving_average.set(
            dataArray=self.datasets["internationalAirlinePassengers"]["pandasDataframe"]["Thousands of Passengers"],
            dataset="internationalAirlinePassengers",
            dataType="Passengers"
        )

        self.results["exponentiallyWeightedMovingAverage"] = exponentially_weighted_moving_average.get_results()