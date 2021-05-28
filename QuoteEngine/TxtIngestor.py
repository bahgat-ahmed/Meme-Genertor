"""Txt file parser class"""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TxtIngestor(IngestorInterface):
    """Parses .Txt file and return a list of QuoteModel classes."""
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses .Txt file and return a list of QuoteModel classes.

        Arguments:
            path {str} -- file to parse location
        Returns:
            List -- List of QuoteModel classes
        """
        # check if file extension is supported by the tool
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        # read text file
        with open(path, 'r', encoding='utf8') as infile:
            # loop over all lines
            for line in infile.readlines():
                # split text on '-'
                line = line.split('-')
                if len(line) > 0:
                    # create a QuoteModel instance object while removing
                    # leading and trailing whitespaces
                    new_quote = QuoteModel(line[0].strip(), line[1].strip())
                    quotes.append(new_quote)

        return quotes
