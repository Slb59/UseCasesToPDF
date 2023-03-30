import os
from datetime import datetime
from fpdf import FPDF

class PDF:
    def __init__(self, name, title):
        self.assets_folder = 'assets'
        self.font = 'Raleway-Light.ttf'
        self.name = name
        self.total_pages = 1
        self.current_page = 1
        self.pdf = FPDF(orientation='L', unit='mm', format='A4')
        self.center = 120
        self.title = title

    def generate_header(self):
        """ generate the header for each pages """
        self.pdf.add_page()
        file = os.path.join(self.assets_folder, self.font)
        self.pdf.add_font(self.font, '', file, uni=True)
        file = os.path.join(self.assets_folder, "logo-occ.png")
        self.pdf.image(file, x=5, y=5)
        self.pdf.set_font(self.font, '', 14)
        self.pdf.text(x=90, y=20,txt=self.title)


    def generate_footer(self):
        """ generate the footer of the page """
        now = datetime.now()
        a_text = "Développeur d'application Python - Sylvie Bricout – Le "
        a_text += f"{now.day}/{now.strftime('%m')}/{now.year}"
        self.pdf.set_font(self.font, '', 12)
        self.pdf.text(x=70, y=205, txt=a_text)
        a_text = f"{self.current_page}/{self.total_pages}"
        self.pdf.text(x=270, y=205, txt=a_text)

    def generate_file(self):
        """ generate the file in the output directory """
        file = os.path.join('output', self.name)
        self.pdf.output(file)

    def add_title(self, a_text: str):
        self.pdf.set_font(self.font, '', 24)
        self.pdf.text(x=self.center - (len(a_text)/2), y=50, txt=a_text)

    def page_img(self, img_name):
        """ generate a page with a image """
        self.generate_header()
        file = os.path.join(self.assets_folder, img_name)
        self.pdf.image(file, x=10, y=30, w=280, h=150)
        self.generate_footer()