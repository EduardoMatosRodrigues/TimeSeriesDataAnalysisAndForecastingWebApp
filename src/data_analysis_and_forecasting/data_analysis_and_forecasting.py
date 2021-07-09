from data_analysis_and_forecasting.mathematical_tools.analysis.augmented_dickey_fuller_test.augmented_dickey_fuller_test import AugmentedDickeyFullerTest
from data_analysis_and_forecasting.mathematical_tools.analysis.error_trend_seasonality_decomposition.error_trend_seasonality_decomposition import ErrorTrendSeasonalityDecomposition
from data_analysis_and_forecasting.mathematical_tools.analysis.exponentially_weighted_moving_average.exponentially_weighted_moving_average import ExponentiallyWeightedMovingAverage
from data_analysis_and_forecasting.mathematical_tools.analysis.hodrick_prescott_filter.hodrick_prescott_filter import HodrickPrescottFilter
from data_analysis_and_forecasting.mathematical_tools.analysis.simple_moving_average.simple_moving_average import SimpleMovingAverage
from data_analysis_and_forecasting.mathematical_tools.forecasting.double_exponential_smoothing.double_exponential_smoothing import DoubleExponentialSmoothing
from data_analysis_and_forecasting.mathematical_tools.forecasting.simple_exponential_smoothing.simple_exponential_smoothing import SimpleExponentialSmoothing
from data_analysis_and_forecasting.mathematical_tools.forecasting.triple_exponential_smoothing.triple_exponential_smoothing import TripleExponentialSmoothing


class DataAnalysisAndForecasting:

    def __init__(self, datasets):

        self.results = {}

        self.datasets = datasets.get()

    def get_results(self, mathematical_tool):

        return self.results[mathematical_tool]

    def set_augmented_dickey_fuller_test(self):

        augmented_dickey_fuller_test = AugmentedDickeyFullerTest()
        augmented_dickey_fuller_test.set(
            dataArray=self.datasets["internationalAirlinePassengers"]["pandasDataframe"]["Thousands of Passengers"],
            dataSet="internationalAirlinePassengers",
            dataType="Passengers",
            dataUnit=None
        )

        self.results["augmentedDickeyFullerTest"] = augmented_dickey_fuller_test

    def set_double_exponential_smoothing(self):

        double_exponential_smoothing = DoubleExponentialSmoothing()
        double_exponential_smoothing.set(
            dataArray=self.datasets["timeSeriesDataSamples"]["pandasDataframe"]["Data with trend"],
            dataSet="timeSeriesDataSamples",
            dataType="Sample data",
            dataUnit=None
        )

        self.results["doubleExponentialSmoothing"] = double_exponential_smoothing

    def set_error_trend_seasonality_decomposition(self):

        error_trend_seasonality_decomposition = ErrorTrendSeasonalityDecomposition()
        error_trend_seasonality_decomposition.set(
            dataArray=self.datasets["internationalAirlinePassengers"]["pandasDataframe"]["Thousands of Passengers"],
            dataSet="internationalAirlinePassengers",
            dataType="Passengers",
            dataUnit=None
        )

        self.results["errorTrendSeasonalityDecomposition"] = error_trend_seasonality_decomposition

    def set_exponentially_weighted_moving_average(self):

        exponentially_weighted_moving_average = ExponentiallyWeightedMovingAverage()
        exponentially_weighted_moving_average.set(
            dataArray=self.datasets["internationalAirlinePassengers"]["pandasDataframe"]["Thousands of Passengers"],
            dataSet="internationalAirlinePassengers",
            dataType="Passengers",
            dataUnit=None
        )

        self.results["exponentiallyWeightedMovingAverage"] = exponentially_weighted_moving_average

    def set_hodrick_prescott_filter(self):

        hodrick_prescott_filter = HodrickPrescottFilter()
        hodrick_prescott_filter.set(
            dataArray=self.datasets["usMacroeconomic"]["pandasDataframe"]["realgdp"],
            dataSet="usMacroeconomic",
            dataType="Real GDP",
            dataUnit="Billions of US$"
        )

        self.results["hodrickPrescottFilter"] = hodrick_prescott_filter

    def set_results(self):

        self.set_hodrick_prescott_filter()
        self.set_error_trend_seasonality_decomposition()
        self.set_simple_moving_average()
        self.set_exponentially_weighted_moving_average()
        self.set_simple_exponential_smoothing()
        self.set_double_exponential_smoothing()
        self.set_triple_exponential_smoothing()
        self.set_augmented_dickey_fuller_test()

    def set_simple_exponential_smoothing(self):

        simple_exponential_smoothing = SimpleExponentialSmoothing()
        simple_exponential_smoothing.set(
            dataArray=self.datasets["dailyFemaleBirthsInCalifornia"]["pandasDataframe"]["Births"],
            dataSet="dailyFemaleBirthsInCalifornia",
            dataType="Births",
            dataUnit=None
        )

        self.results["simpleExponentialSmoothing"] = simple_exponential_smoothing

    def set_simple_moving_average(self):

        simple_moving_average = SimpleMovingAverage()
        simple_moving_average.set(
            dataArray=self.datasets["internationalAirlinePassengers"]["pandasDataframe"]["Thousands of Passengers"],
            dataSet="internationalAirlinePassengers",
            dataType="Passengers",
            dataUnit=None
        )

        self.results["simpleMovingAverage"] = simple_moving_average

    def set_triple_exponential_smoothing(self):

        triple_exponential_smoothing = TripleExponentialSmoothing()
        triple_exponential_smoothing.set(
            dataArray=self.datasets["internationalAirlinePassengers"]["pandasDataframe"]["Thousands of Passengers"],
            dataSet="internationalAirlinePassengers",
            dataType="Passengers",
            dataUnit=None
        )

        self.results["tripleExponentialSmoothing"] = triple_exponential_smoothing
