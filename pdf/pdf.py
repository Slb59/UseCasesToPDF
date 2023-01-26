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
        self.total_pages = 1
        self.current_page = 1
        self.pdf = ''

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
        a_text = f"{self.current_page}/{self.total_pages}"
        self.pdf.text(x=270, y=205, txt=a_text)


class PDFWireframe(PDF):
    """ generate pdf for wireframes """
    def __init__(self, name, parameters):
        super().__init__(name, parameters)

    def generate_menu(self):

        self.pdf.set_font(self.font, '', 14)
        a_text = "LES WIREFRAMES VERSION MOBILES"
        self.pdf.text(x=5, y=45, txt=a_text)
        self.pdf.set_font(self.font, '', 12)
        a_text = "Les fonctionnalités"
        self.pdf.text(x=5, y=60, txt=a_text)

        a_text = "La page de connexion"
        self.pdf.text(x=20, y=80, txt=a_text)
        page_pos_x = 195
        self.pdf.text(x=page_pos_x, y=80, txt="2")
        a_text = "La page interface de chat"
        self.pdf.text(x=20, y=90, txt=a_text)
        self.pdf.text(x=page_pos_x, y=90, txt="3")
        a_text = "La page du calendrier"
        self.pdf.text(x=20, y=100, txt=a_text)
        self.pdf.text(x=page_pos_x, y=100, txt="4")
        a_text = "La page de gestion des tâches"
        self.pdf.text(x=20, y=110, txt=a_text)
        self.pdf.text(x=page_pos_x, y=110, txt="5")
        a_text = "La page tableau de bord"
        self.pdf.text(x=20, y=120, txt=a_text)
        self.pdf.text(x=page_pos_x, y=120, txt="6")

        for i in range(5):
            a_text = ''
            for j in range(80):
                a_text += '_'
            self.pdf.text(x=50, y=80+i*10, txt=a_text)


class PDFWireframeD(PDFWireframe):
    """ generate pdf for wireframes for desktop """
    def __init__(self, name, parameters):
        super().__init__(name, parameters)

    def generate_p1(self):
        self.pdf.add_page()
        self.current_page += 1
        self.total_pages += 1
        a_text = "La page de connexion"
        self.pdf.text(x=10, y=10, txt=a_text)
        file = os.path.join(self.img_directory, "page_de_connexion (M) - NB.png")
        self.pdf.image(file, x=10, y=20, w=67, h=117)
        file = os.path.join(self.img_directory, "page_de_creation_de_compte tuteur (M) - NB.png")
        self.pdf.image(file, x=80, y=20, w=67, h=117)
        file = os.path.join(self.img_directory, "page_de_creation_de_compte eleve(M) - NB.png")
        self.pdf.image(file, x=150, y=20, w=67, h=117)

    def generate_p2(self):
        self.pdf.add_page()
        self.current_page += 1
        self.total_pages += 1
        a_text = "La page interface de chat"
        self.pdf.text(x=10, y=10, txt=a_text)
        file = os.path.join(self.img_directory, "page_interface_chat_tuteur (M) - NB.png")
        self.pdf.image(file, x=10, y=20, w=67, h=117)
        file = os.path.join(self.img_directory, "page_interface_chat_eleve (M) - NB.png")
        self.pdf.image(file, x=80, y=20, w=67, h=117)
        file = os.path.join(self.img_directory, "page contact tuteur (M) - NB.png")
        self.pdf.image(file, x=150, y=20, w=67, h=117)
        file = os.path.join(self.img_directory, "page contact eleve (M) - NB.png")
        self.pdf.image(file, x=220, y=20, w=67, h=117)

    def generate_p3(self):
        self.pdf.add_page()
        self.current_page += 1
        self.total_pages += 1
        a_text = "La page calendrier"
        self.pdf.text(x=10, y=10, txt=a_text)
        file = os.path.join(self.img_directory, "page calendrier tuteur (M) - NB.png")
        self.pdf.image(file, x=10, y=20, w=67, h=117)
        file = os.path.join(self.img_directory, "page calendrier elève (M) - NB.png")
        self.pdf.image(file, x=80, y=20, w=67, h=117)

    def generate(self):
        self.generate_header()

        self.generate_menu()
        self.generate_footer()

        self.generate_p1()
        self.generate_footer()

        self.generate_p2()
        self.generate_footer()

        self.generate_p3()
        self.generate_footer()

        self.generate_file()

class PDFWireframeM(PDFWireframe):
    """ generate pdf for wireframes mobiles """
    def __init__(self, name, parameters):
        super().__init__(name, parameters)

    def generate_p1(self):
        self.pdf.add_page()
        self.current_page += 1
        self.total_pages += 1
        a_text = "La page de connexion"
        self.pdf.text(x=10, y=10, txt=a_text)
        file = os.path.join(self.img_directory, "page_de_connexion (M) - NB.png")
        self.pdf.image(file, x=10, y=20, w=67, h=117)
        file = os.path.join(self.img_directory, "page_de_creation_de_compte tuteur (M) - NB.png")
        self.pdf.image(file, x=80, y=20, w=67, h=117)
        file = os.path.join(self.img_directory, "page_de_creation_de_compte eleve(M) - NB.png")
        self.pdf.image(file, x=150, y=20, w=67, h=117)

    def generate_p2(self):
        self.pdf.add_page()
        self.current_page += 1
        self.total_pages += 1
        a_text = "La page interface de chat"
        self.pdf.text(x=10, y=10, txt=a_text)
        file = os.path.join(self.img_directory, "page_interface_chat_tuteur (M) - NB.png")
        self.pdf.image(file, x=10, y=20, w=67, h=117)
        file = os.path.join(self.img_directory, "page_interface_chat_eleve (M) - NB.png")
        self.pdf.image(file, x=80, y=20, w=67, h=117)
        file = os.path.join(self.img_directory, "page contact tuteur (M) - NB.png")
        self.pdf.image(file, x=150, y=20, w=67, h=117)
        file = os.path.join(self.img_directory, "page contact eleve (M) - NB.png")
        self.pdf.image(file, x=220, y=20, w=67, h=117)

    def generate_p3(self):
        self.pdf.add_page()
        self.current_page += 1
        self.total_pages += 1
        a_text = "La page calendrier"
        self.pdf.text(x=10, y=10, txt=a_text)
        file = os.path.join(self.img_directory, "page calendrier tuteur (M) - NB.png")
        self.pdf.image(file, x=10, y=20, w=67, h=117)
        file = os.path.join(self.img_directory, "page calendrier elève (M) - NB.png")
        self.pdf.image(file, x=80, y=20, w=67, h=117)

    def generate(self):
        self.generate_header()

        self.generate_menu()
        self.generate_footer()

        self.generate_p1()
        self.generate_footer()

        self.generate_p2()
        self.generate_footer()

        self.generate_p3()
        self.generate_footer()

        self.generate_file()


class PDFUml(PDF):
    """ generate pdf for uml diagramme """
    def __init__(self, name, parameters):
        super().__init__(name, parameters)

    def generate(self):
        self.generate_header()

        # add uml diagram
        file = os.path.join(self.img_directory, "uml.png")
        self.pdf.image(file, x=5, y=30, w=290, h=180)

        self.generate_footer()
        self.generate_file()

