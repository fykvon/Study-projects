from PIL import Image, ImageDraw, ImageFont, ImageColor


class TicketFiller:

    def __init__(self, passanger_name, where, to, departure_date):
        self.passanger_name = passanger_name
        self.to = to
        self.departure_date = departure_date
        self.where = where
        self.template = 'images/ticket_template.png'

    def template_maker(self):
        im = Image.open(self.template)
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("arial.ttf", size=16)
        y = 120
        param_list = [self.passanger_name, self.where, self.to]
        for i in param_list:
            draw.text((50, y), i, font=font, fill=ImageColor.colormap['black'])
            y = y + 70
        draw.text((280, 260), self.departure_date, font=font, fill=ImageColor.colormap['black'])
        im.show()
