class QuoteModel:
    """QuoteModel class"""
    def __init__(self, body, author):
        self.author = author
        self.body = body

    def __repr__(self):
        """Overriding object class __repr__ method"""
        return f"{self.body} - {self.author}"
