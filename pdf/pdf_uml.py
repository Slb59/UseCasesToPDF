from pdf import PDF
import os
from logs import LOGGER
from fpdf import FPDF


class PDFUml(PDF):
    """ generate pdf for uml diagramme """
    def __init__(self, name, parameters):
        super().__init__(name, parameters)

    def generate(self):
        self.generate_header()

        # add uml diagram
        file = os.path.join(self.img_directory, "uml2.png")
        self.pdf.image(file, x=5, y=30, w=290, h=160)

        self.generate_footer()
        self.generate_file()
