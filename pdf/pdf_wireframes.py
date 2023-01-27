from pdf import PDF
import os
from logs import LOGGER
from fpdf import FPDF


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
        images_w = 95
        image_h = 75
        file = os.path.join(self.img_directory, "page_de_connexion (D) - NB.png")
        self.pdf.image(file, x=10, y=20, w=images_w, h=image_h)
        file = os.path.join(self.img_directory, "page_de_creation_de_compte tuteur (D) - NB.png")
        self.pdf.image(file, x=10 + images_w + 5, y=20, w=images_w, h=image_h)
        file = os.path.join(self.img_directory, "page_de_creation_de_compte élève (D) - NB.png")
        self.pdf.image(file, x=10 + images_w + 5, y=20 + image_h + 5, w=images_w, h=image_h)

    def generate_p2(self):
        self.pdf.add_page()
        self.current_page += 1
        self.total_pages += 1
        a_text = "La page interface de chat"
        self.pdf.text(x=10, y=10, txt=a_text)
        images_w = 95
        image_h = 75
        file = os.path.join(self.img_directory, "page_interface_chat_tuteur (D) - NB.jpg")
        self.pdf.image(file, x=10, y=20, w=images_w, h=image_h)
        file = os.path.join(self.img_directory, "page_interface_chat_eleve (D) - NB.jpg")
        self.pdf.image(file, x=10 + images_w + 5, y=20, w=images_w, h=image_h)
        file = os.path.join(self.img_directory, "page contact tuteur (D) - NB.png")
        self.pdf.image(file, x=10, y=20 + image_h + 5, w=images_w, h=image_h)
        file = os.path.join(self.img_directory, "page contact eleve (D) - NB.png")
        self.pdf.image(file, x=10 + images_w + 5, y=20 + image_h + 5, w=images_w, h=image_h)

    def generate_p3(self):
        self.pdf.add_page()
        self.current_page += 1
        self.total_pages += 1
        a_text = "La page calendrier"
        self.pdf.text(x=10, y=10, txt=a_text)
        images_w = 95
        image_h = 75
        file = os.path.join(self.img_directory, "page calendrier tuteur (D) - NB.jpg")
        self.pdf.image(file, x=10, y=20, w=images_w, h=image_h)
        file = os.path.join(self.img_directory, "page calendrier eleve (D) - NB.png")
        self.pdf.image(file, x=10 + images_w + 5, y=20, w=images_w, h=image_h)

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
