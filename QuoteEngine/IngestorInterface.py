"""The base abstract ingestor class from which all other ingestors inherit."""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """Base abstract class that check if extension is supported by the tool
    and provide the signature for the abstract parse method."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if file extension is supportedd by the tool.
        Arguments:
            path {str} -- file to parse location
        Returns:
            bool -- whether file extension is supported
        """
        # get file extension
        extension = path.split('.')[-1]
        return extension in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Create a list of QuoteModel classes. Subclasses must override this
        method by applying appropriate parsing depending on the file extension.

        Arguments:
            path {str} -- file to parse location
        Returns:
            List -- List of QuoteModel classes
        """
        pass
