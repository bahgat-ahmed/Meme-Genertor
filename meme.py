import os
import random
import argparse

from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine

def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote
    Arguments:
        path {str} -- path to an image file
        body {str} -- quote body to add to the image
        author {str} -- quote author to add to the image
    Returns:
        path {str} -- generated meme image file location
    """
    img = None
    quote = None

    if path is None:
        # find all images within the images images_path directory
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        # parse all quote files into quote and author
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # instantiate ArgumentParser with a welcome message
    parser = argparse.ArgumentParser(description="Welcome to Meme Generator!")
    # optional path argument
    parser.add_argument('--path', type=str, default=None,
                        help="path to an image file")
    # optional body argument
    parser.add_argument('--body', type=str, default=None,
                        help="quote body to add to the image")
    # optional author argument
    parser.add_argument('--author', type=str, default=None,
                        help="quote author to add to the image")
    # parse arguments
    args = parser.parse_args()
    # generate meme
    print(generate_meme(args.path, args.body, args.author))
