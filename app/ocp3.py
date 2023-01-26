import os
import app


from logs import LOGGER
from pdf import PDFUml, PDFWireframeM


class OCP3:
    def __init__(self, parameters):
        self.version = app.__version__
        self.output_directory = parameters.output_directory
        self.fonts_directory = parameters.fonts_directory
        self.img_directory = parameters.img_directory
        self.check_directories()


        LOGGER.debug('Initialisation de OCP3')

        self.uml_file = PDFUml('uml.pdf', parameters)
        self.wireframesm = PDFWireframeM('wireframes(m).pdf', parameters)

    def generate_files(self):
        self.uml_file.generate()
        self.wireframesm.generate()

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


