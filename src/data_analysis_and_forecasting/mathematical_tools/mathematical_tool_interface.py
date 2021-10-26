from abc import ABC, abstractmethod


class MathematicalToolInterface(ABC):

    def __init__(self):

        self.explanation = None

        self.input_data_info = {
            "dataArray": None,
            "dataSet": None,
            "dataType": None,
            "dataUnit": None
        }

        self.results = {}

        self.figure = None

    def get_explanation(self):

        return self.explanation

    def get_figure(self):

        return self.figure

    def get_input_data_info(self):

        return self.input_data_info

    def get_results(self):

        return self.results

    @abstractmethod
    def _set_explanation(self):

        pass

    @abstractmethod
    def _set_figure(self):

        pass

    def _set_input_data_info(self, **kwargs):

        self.input_data_info["dataArray"] = kwargs["dataArray"]
        self.input_data_info["dataSet"] = kwargs["dataSet"]
        self.input_data_info["dataType"] = kwargs["dataType"]
        self.input_data_info["dataUnit"] = kwargs["dataUnit"]

    @abstractmethod
    def _set_results(self):

        pass

    def set(self, **kwargs):

        self._set_input_data_info(**kwargs)
        self._set_explanation()
        self._set_results()
        self._set_figure()
