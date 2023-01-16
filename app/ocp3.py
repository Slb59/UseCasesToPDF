import os
import app

from fpdf import FPDF
from logs import LOGGER
from uml import *


class OCP3:
    def __init__(self, parameters):
        self.version = app.__version__
        self.output_directory = parameters.output_directory
        self.fonts_directory = parameters.fonts_directory
        self.img_directory = parameters.img_directory
        self.check_directories()

        self.font = 'Raleway-Light.ttf'
        LOGGER.debug('Initialisation de OCP3')

    def check_directories(self):
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)
        if not os.path.exists(self.fonts_directory) \
                or not os.path.exists(self.img_directory):
            raise Exception(f'Manque le répertoire {self.fonts_directory} '
                            f'ou le répertoire {self.img_directory}')

    def __str__(self):
        return 'OCP3 Generation'

    def usecase_connexion(self):
        use_case = UseCaseConnexion()

    def generate(self):
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()

        file = os.path.join(self.fonts_directory, self.font)
        pdf.add_font(self.font, '', file, uni=True)
        pdf.set_font(self.font, '', 10)

        file = os.path.join(self.img_directory, "logo_dev4u.png")
        pdf.image(file, x=0, y=0, w=50, h=25)

        pdf.add_page('assets/pdf/uml_page_de_connexion.pdf')

        file = os.path.join(self.output_directory, "test1.pdf")
        pdf.cell(200, 10, txt="this is the programming of creating pdf file", ln=1, align="L")

        pdf.output(file)
