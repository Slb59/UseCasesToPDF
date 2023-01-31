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

        fleche = os.path.join(self.img_directory, "fleche.jpg")

        table_of_content = [[2, 'page 2', "La page de connexion"],
                            [3, 'page 3', "La page interface de chat"],
                            [4, 'page 4', "La page du calendrier"],
                            [5, 'page 5', "La page de gestion des tâches"],
                            [6, 'page 6', "La page tableau de bord"]]

        posx = 35
        posy = 80
        for elem in table_of_content:
            self.pdf.image(fleche, x=20, y=posy - 5, w=10, h=5)
            self.pdf.text(x=posx, y=posy, txt=elem[2])
            posy += 10

        for i in range(5):
            a_text = ''
            for j in range(80):
                a_text += '_'
            self.pdf.text(x=80, y=80+i*10, txt=a_text)

        posy = 55
        self.pdf.set_text_color(218, 33, 33)
        for elem in table_of_content:
            page_pos_x = 230
            new_link = self.pdf.add_link()
            self.pdf.set_link(new_link, y=0.0, page=elem[0])
            self.pdf.set_xy(page_pos_x, posy)
            self.pdf.write(50, elem[1], link=new_link)
            posy += 10
        self.pdf.set_text_color(0, 0, 0)


class PDFWireframeD(PDFWireframe):
    """ generate pdf for wireframes for desktop """
    def __init__(self, name, parameters):
        super().__init__(name, parameters)

    def generate_p1(self):
        self.pdf.add_page()
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
        a_text = "La page calendrier"
        self.pdf.text(x=10, y=10, txt=a_text)
        images_w = 95
        image_h = 75
        file = os.path.join(self.img_directory, "page calendrier tuteur (D) - NB.jpg")
        self.pdf.image(file, x=10, y=20, w=images_w, h=image_h)
        file = os.path.join(self.img_directory, "page calendrier tuteur - Ajouter (D).jpg")
        self.pdf.image(file, x=10 + images_w + 5, y=20, w=images_w, h=image_h)
        file = os.path.join(self.img_directory, "page calendrier eleve (D) - NB.png")
        self.pdf.image(file, x=10, y=20 + image_h + 5, w=images_w, h=image_h)

    def generate_p4(self):
        self.pdf.add_page()
        a_text = "La page gestion des tâches"
        self.pdf.text(x=10, y=10, txt=a_text)
        images_w = 95
        image_h = 75
        file = os.path.join(self.img_directory, "page gestion taches tuteur (D).png")
        self.pdf.image(file, x=10, y=20, w=images_w, h=image_h)
        file = os.path.join(self.img_directory, "page gestion taches eleve (D).png")
        self.pdf.image(file, x=10 + images_w + 5, y=20, w=images_w, h=image_h)

    def generate_p5(self):
        self.pdf.add_page()
        a_text = "La page tableau de bord"
        self.pdf.text(x=10, y=10, txt=a_text)
        images_w = 95
        image_h = 75
        file = os.path.join(self.img_directory, "tableau de bord tuteur (D).png")
        self.pdf.image(file, x=10, y=20, w=images_w, h=image_h)


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

        self.generate_p4()
        self.generate_footer()

        self.generate_p5()
        self.generate_footer()

        self.generate_file()


class PDFWireframeM(PDFWireframe):
    """ generate pdf for wireframes mobiles """
    def __init__(self, name, parameters):
        super().__init__(name, parameters)

    def generate_p1(self):
        self.pdf.add_page()
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
        a_text = "La page calendrier"
        self.pdf.text(x=10, y=10, txt=a_text)
        images_w = 67
        image_h = 117
        file = os.path.join(self.img_directory, "page calendrier tuteur (M) - NB.png")
        self.pdf.image(file, x=10, y=20, w=images_w, h=image_h)
        file = os.path.join(self.img_directory, "page calendrier tuteur - ajouter (M).png")
        self.pdf.image(file, x=10 + images_w + 5, y=20, w=images_w, h=image_h)
        file = os.path.join(self.img_directory, "page calendrier elève (M) - NB.png")
        self.pdf.image(file, x=10 + 2*images_w + 10, y=20, w=images_w, h=image_h)

    def generate_p4(self):
        self.pdf.add_page()
        a_text = "La page gestion des tâches"
        self.pdf.text(x=10, y=10, txt=a_text)
        images_w = 67
        image_h = 117
        file = os.path.join(self.img_directory, "page gestion taches tuteur (M).png")
        self.pdf.image(file, x=10, y=20, w=images_w, h=image_h)
        file = os.path.join(self.img_directory, "page gestion taches eleve (M).png")
        self.pdf.image(file, x=10 + images_w + 5, y=20, w=images_w, h=image_h)

    def generate_p5(self):
        self.pdf.add_page()
        a_text = "La page tableau de bord"
        self.pdf.text(x=10, y=10, txt=a_text)
        images_w = 67
        image_h = 117
        file = os.path.join(self.img_directory, "tableau de bord tuteur (M).png")
        self.pdf.image(file, x=10, y=20, w=images_w, h=image_h)


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

        self.generate_p4()
        self.generate_footer()

        self.generate_p5()
        self.generate_footer()

        self.generate_file()
