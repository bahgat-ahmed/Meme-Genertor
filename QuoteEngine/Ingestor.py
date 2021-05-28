"""Main ingestor class that encapsulates all ingestors."""
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .TxtIngestor import TxtIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """Main ingestor class that encapsulates all ingestors. It provides
    one interface to load any supported file type."""

    ingestors = [DocxIngestor, CSVIngestor, TxtIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Select appropriate ingestor based on file extension."""
        # loop over all ingestors
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                try:
                    return ingestor.parse(path)
                except Exception as e:
                    print(e)
