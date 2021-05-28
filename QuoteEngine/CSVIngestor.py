"""CSV file parser class"""
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import pandas

class CSVIngestor(IngestorInterface):
    """Parses .CSV file and return a list of QuoteModel classes."""
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses .CSV file and return a list of QuoteModel classes.

        Arguments:
            path {str} -- file to parse location
        Returns:
            List -- List of QuoteModel classes
        """
        # check if file extension is supported by the tool
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        # read csv file
        df = pandas.read_csv(path, header=0)
        # loop over all rows
        for index, row in df.iterrows():
            # create a QuoteModel instance object
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
