import os
from logs import LOGGER
from fpdf import FPDF
from datetime import datetime


class PDF:
    def __init__(self, name, parameters):
        self.output_directory = parameters.output_directory
        self.fonts_directory = parameters.fonts_directory
        self.img_directory = parameters.img_directory
        self.font = 'Raleway-Light.ttf'
        self.name = name

    def generate_header(self):
        self.pdf = FPDF(orientation='L', unit='mm', format='A4')
        self.pdf.add_page()

        file = os.path.join(self.fonts_directory, self.font)
        self.pdf.add_font(self.font, '', file, uni=True)

        file = os.path.join(self.img_directory, "logo_learnhome.png")
        self.pdf.image(file, x=5, y=5, w=50, h=25)
        self.pdf.set_font(self.font, '', 14)
        self.pdf.text(x=70, y=20, txt="DEVELOPPEMENT D'UN SITE WEB DE MISE EN RELATION ELEVE - TUTEUR")

    def generate_file(self):
        """ generate the file in the output directory """
        file = os.path.join(self.output_directory, self.name)
        LOGGER.debug(f'generate file  {file}')
        self.pdf.output(file)

    def generate_footer(self):
        """ generate the footer of the page """
        file = os.path.join(self.img_directory, "logo_dev4u.png")
        self.pdf.image(file, x=5, y=190, w=50, h=25)
        now = datetime.now()
        a_text = "Les services du numérique – Sylvie Bricout – Le "
        a_text += f"{now.day}/{now.month}/{now.year}"
        self.pdf.set_font(self.font, '', 12)
        self.pdf.text(x=70, y=205, txt=a_text)
        a_text = f"{self.pdf.page_no()}/{self.pdf.alias_nb_pages()}"
        self.pdf.text(x=270, y=205, txt=a_text)






