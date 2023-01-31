import os
import app


from logs import LOGGER
from pdf import PDFUml, PDFWireframeM, PDFWireframeD, PDFUserStory


class OCP3:
    def __init__(self, parameters):
        self.version = app.__version__
        self.output_directory = parameters.output_directory
        self.fonts_directory = parameters.fonts_directory
        self.img_directory = parameters.img_directory
        self.check_directories()

        LOGGER.debug('Initialisation de OCP3')

        self.uml_file = PDFUml('uml.pdf', parameters)
        self.wireframes_m = PDFWireframeM('wireframes(M).pdf', parameters)
        self.wireframes_d = PDFWireframeD('wireframes(D).pdf', parameters)
        self.user_stories = PDFUserStory('user_stories.pdf', parameters)

    def generate_files(self):
        print("Generation du fichier uml")
        self.uml_file.generate()
        print("generation des wireframes mobiles")
        self.wireframes_m.generate()
        print("generation des wireframes desktop")
        self.wireframes_d.generate()
        print("generate user stories")
        self.user_stories.load_csv()
        self.user_stories.generate()

    def check_directories(self):
        """ check the directories exists """
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)
        if not os.path.exists(self.fonts_directory) \
                or not os.path.exists(self.img_directory):
            raise Exception(f'Manque le répertoire {self.fonts_directory} '
                            f'ou le répertoire {self.img_directory}')

    def __str__(self):
        return 'OCP3 Generation'

    def usecase_connexion(self):
        pass
        # use_case = UseCaseConnexion()


