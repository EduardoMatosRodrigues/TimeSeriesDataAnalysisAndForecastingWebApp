import pandas as pd


class Datasets:

    def __init__(self):

        self.datasets = {}

    def get(self):

        return self.datasets

    def set(self):

        self.set_international_airline_passengers()
        self.set_time_series_data_samples()
        self.set_us_macroeconomic()

    def set_international_airline_passengers(self):

        self.datasets["internationalAirlinePassengers"] = {
            "explanation": "International airline passengers data (1949 - 1960)",
            "pandasDataframe": pd.read_csv(
                "datasets/csv_files/international-airline-passengers-dataset.csv",
                index_col="Month",
                parse_dates=True
            )
        }

        self.datasets["internationalAirlinePassengers"]["pandasDataframe"].dropna(inplace=True)
        self.datasets["internationalAirlinePassengers"]["pandasDataframe"].index = \
            pd.to_datetime(self.datasets["internationalAirlinePassengers"]["pandasDataframe"].index)

        self.datasets["internationalAirlinePassengers"]["pandasDataframe"].index.freq = "MS"

    def set_time_series_data_samples(self):

        self.datasets["timeSeriesDataSamples"] = {
            "explanation": "Time series data samples (1950 - 1959)",
            "pandasDataframe": pd.read_csv(
                "datasets/csv_files/time-series-data-samples.csv",
                index_col=0,
                parse_dates=True
            )
        }

    def set_us_macroeconomic(self):

        self.datasets["usMacroeconomic"] = {
            "explanation": "US macroeconomic data (1959 - 2009)",
            "pandasDataframe": pd.read_csv("datasets/csv_files/us-macroeconomic-dataset.csv")
        }

        self.datasets["usMacroeconomic"]["pandasDataframe"].set_index("date", inplace=True)
        self.datasets["usMacroeconomic"]["pandasDataframe"].index = \
            pd.to_datetime(self.datasets["usMacroeconomic"]["pandasDataframe"].index)
