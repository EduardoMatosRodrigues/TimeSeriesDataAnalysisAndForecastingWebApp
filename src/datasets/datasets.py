import pandas as pd


class Datasets:

    def __init__(self):

        self.datasets = {}

    def get(self):

        return self.datasets

    def set(self):

        self.set_daily_female_births_in_california()
        self.set_international_airline_passengers()
        self.set_time_series_data_sample_with_trend()
        self.set_time_series_data_samples_with_causality()
        self.set_us_macroeconomic()

    def set_daily_female_births_in_california(self):

        self.datasets["dailyFemaleBirthsInCalifornia"] = {
            "explanation": "Total number of female births recording in California, USA (1959)",
            "pandasDataframe": pd.read_csv(
                "datasets/csv_files/daily-female-births-in-california.csv",
                index_col="Date",
                parse_dates=True
            )
        }

        self.datasets["dailyFemaleBirthsInCalifornia"]["pandasDataframe"].index = \
            pd.to_datetime(self.datasets["dailyFemaleBirthsInCalifornia"]["pandasDataframe"].index)

        self.datasets["dailyFemaleBirthsInCalifornia"]["pandasDataframe"].index.freq = "D"

    def set_international_airline_passengers(self):

        self.datasets["internationalAirlinePassengers"] = {
            "explanation": "International airline passengers data (1949 - 1960)",
            "pandasDataframe": pd.read_csv(
                "datasets/csv_files/international-airline-passengers.csv",
                index_col="Month",
                parse_dates=True
            )
        }

        self.datasets["internationalAirlinePassengers"]["pandasDataframe"].dropna(inplace=True)
        self.datasets["internationalAirlinePassengers"]["pandasDataframe"].index = \
            pd.to_datetime(self.datasets["internationalAirlinePassengers"]["pandasDataframe"].index)

        self.datasets["internationalAirlinePassengers"]["pandasDataframe"].index.freq = "MS"

    def set_time_series_data_sample_with_trend(self):

        self.datasets["timeSeriesDataSampleWithTrend"] = {
            "explanation": "Time series data sample with trend (1950 - 1959)",
            "pandasDataframe": pd.read_csv(
                "datasets/csv_files/time-series-data-sample-with-trend.csv",
                index_col="Date",
                parse_dates=True
            )
        }

    def set_time_series_data_samples_with_causality(self):

        self.datasets["timeSeriesDataSampleWithGrangerCausality"] = {
            "explanation": "Time series data samples with Granger causality (1950 - 1959)",
            "pandasDataframe": pd.read_csv(
                "datasets/csv_files/time-series-data-samples-with-granger-causality.csv",
                index_col="Date",
                parse_dates=True
            )
        }

    def set_us_macroeconomic(self):

        self.datasets["usMacroeconomic"] = {
            "explanation": "US macroeconomic data (1959 - 2009)",
            "pandasDataframe": pd.read_csv("datasets/csv_files/us-macroeconomic.csv")
        }

        self.datasets["usMacroeconomic"]["pandasDataframe"].set_index("date", inplace=True)
        self.datasets["usMacroeconomic"]["pandasDataframe"].index = \
            pd.to_datetime(self.datasets["usMacroeconomic"]["pandasDataframe"].index)
