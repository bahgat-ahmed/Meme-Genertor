"""PDF file parser class"""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import random
import os
import subprocess

class PDFIngestor(IngestorInterface):
    """Parses .PDF file and return a list of QuoteModel classes."""
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses .PDF file and return a list of QuoteModel classes.

        Arguments:
            path {str} -- file to parse location
        Returns:
            List -- List of QuoteModel classes
        """
        # check if file extension is supported by the tool
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        # temporary file location
        tmp = f'.{random.randint(0, 10000000)}.txt'
        # convert PDF file to text file using command line tool
        call = subprocess.call(['pdftotext', path, tmp])
        # open the text file
        file = open(tmp, "r")

        quotes = []
        # loop over all lines
        for line in file.readlines():
            # remove new line, leading and trailing whitespaces
            line = line.strip('\n').strip()
            # split text on '-'
            line = line.split('-')
            # remove empty strings from list
            line = list(filter(lambda x: x != '', line))
            # check if line is not empty
            if len(line) > 0:
                # create a QuoteModel instance object
                new_quote = QuoteModel(line[0], line[1])
                quotes.append(new_quote)
        # close the text file
        file.close()
        # delete the temporary text file
        os.remove(tmp)

        return quotes
