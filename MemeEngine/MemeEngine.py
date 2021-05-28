"""Resize image, and Quote and Author on it"""
from PIL import Image, ImageDraw, ImageFont
import random

class MemeEngine:
    """class to resize image, and Quote and Author on it"""
    def __init__(self, img_out_path='./static'):
        """Initialize instance.
        Arguments:
            img_out_path {str} -- edited images output location
        """
        self.img_out_path = img_out_path

    def make_meme(self, img_path, text=None, author=None, width=500) -> str:
        """Make a meme by resiziing image and adding text on it.
        Arguments:
            img_path {str} -- input image file locationive
            text {str} -- quote to insert on the image
            author {str} -- quote author to insert on the image
            width {int} -- width to resize the image to while length will be
            automatically adjusted to preserve the image's aspect ratio
        Returns:
            str -- edited image file location
        """
        # open image
        img = Image.open(img_path)
        # get input image file extension
        extension = img_path.split('.')[-1]
        # if required width is greater than the maximum allowed or less than
        # zero then set it to be the same maximum, and default value of 500px
        if width > 500 or width <= 0:
            width = 500

        ratio = width / float(img.size[0])
        # adjust height automatically to preserve images' aspect ratio
        height = int(ratio * float(img.size[1]))
        # resize image
        img = img.resize((width, height), Image.NEAREST)

        # insert quote and author text onto image
        if text is not None and author is not None:
            draw = ImageDraw.Draw(img)
            font_size = int(height / 16)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf',
                    size=font_size)
            # get text display x axis
            x_min = 0
            x_max = int(img.size[0]/12)
            x_range = random.randint(x_min, x_max)

            lines = [text, " > " + author]
            line_height = font.getsize('hg')[1]
            # get text display y axis
            y_min = int(img.size[1]/24)
            y_max = int(img.size[1])
            # leave some space below text to avoid text getting out of image
            y_max -= ((len(lines) + 1) * line_height)
            y_range = random.randint(y_min, y_max)

            # draw text
            for line in lines:
                draw.text((x_range, y_range), line, font=font)
                y_range += line_height

        # save new edited image to the required output location
        out_path = f'{self.img_out_path}/{random.randint(0, 10000000)}.{extension}'
        img.save(out_path)
        return out_path

    def __repr__(self):
        return f'Image Output Path: {self.img_out_path}'

if __name__ == '__main__':
    # instantiate a MemeEngine object
    post_card = MemeEngine('./static')
    print(post_card)
    post_card.make_meme('./_data/photos/dog/xander_1.jpg', 'hello', 'one', 500)
