from pdf import PDF
import os
from logs import LOGGER
from fpdf import FPDF



class PDFUserStory(PDF):
    """ generate pdf for user stories """

    def __init__(self, name, parameters):
        super().__init__(name, parameters)

    def load_odt(self):
        pass
        # file = os.path.join(self.img_directory, "user_stories.odt")
        # textdoc = load(file)
        # allparas = textdoc.getElementsByType(text.P)
        # teletype.extractText(allparas[0])
        # print(teletype)
