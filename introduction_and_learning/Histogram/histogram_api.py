__all__ = [
    "HistogramInterface"
]
from abc import abstractmethod, ABCMeta


class HistogramInterface(metaclass=ABCMeta):
    """
    HistogramInterface is basic interface for creating histogram from various
    file types classes.

    HistogramInterface is abstract class. Methods that required are
        read_data(file_path)
        create(data_input)
        generate_report(histogram, output_type, path)
    """

    @abstractmethod
    def read_data(self, file_path: str) -> str:
        """
        This method handling opening and reading from given file. Type of this
        file is given in class definition.

        Parameters
        ----------
            file_path: string, required
                Localisation of file which data should be read from.

        Returns
        -------
        Method return before read data on success or information
        "File does not have [file extension like .txt] extension." on
        failure.

        Exaples
        -------
        >>> histogram_txt.read_data("myDoc/file.txt")
        >>> histogram_json.read_data("myDoc/file.json")
        """
        raise NotImplementedError

    @abstractmethod
    def create(self, data_input: str) -> dict:
        """
        Method creates a histogram using dictionary in style {"value": amount}

        Parameters
        __________
        data_input: string, required
            String that is used as data to create histogram based on amount
            of specified words in this sting. Characters like ".", "," are not
            included.

        Returns
        -------
        Dictionary with is created based on data_input attribute.

        Example
        -------
        >>> histogram_txt.create("very long string")
        """
        raise NotImplementedError

    @abstractmethod
    def generate_report(self, histogram: dict, output_type: str = "html", path: str = "report") -> bool:
        """
        Create a human readable report in file type specified in output_type
        param is useful for data analyse.

        Parameters
        ----------
        histogram: dictionary, required
            Histogram data in dictionary data structure {"value": amount},
            e. g. dictionary returned by create method.
        output_type: string, optional
            Document type of which will be generated report. This param can be:
            html, csv, txt another will cause return False. Default value is html.
        path: string, optional
            Destination with file name where report be generated. Filne must not
            contain expression like .txt, .html.

        Returns
        -------
        Return True if report was generated successfully and False on failure.

        Example
        -------
        >>> histogram_txt.generate_report(dictonary, "html", "report")
        """
        raise NotImplementedError
