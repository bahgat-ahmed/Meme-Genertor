"""DOCx file parser class"""
from typing import List
import docx
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DocxIngestor(IngestorInterface):
    """Parses .DOCx file and return a list of QuoteModel classes."""
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses .DOCx file and return a list of QuoteModel classes.

        Arguments:
            path {str} -- file to parse location
        Returns:
            List -- List of QuoteModel classes
        """
        # check if file extension is supported by the tool
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)
        # loop over all paragraphs
        for para in doc.paragraphs:
            # check if text is not empty
            if para.text != "":
                # split text on '-'
                parse = para.text.split('-')
                # create a QuoteModel instance object while removing
                # leading and trailing whitespaces
                new_quote = QuoteModel(parse[0].strip(), parse[1].strip())
                quotes.append(new_quote)

        return quotes
