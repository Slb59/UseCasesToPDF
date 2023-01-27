import csv
import os
import textwrap

from pdf import PDF
from logs import LOGGER
from fpdf import FPDF
from .story import Story



class PDFUserStory(PDF):
    """ generate pdf for user stories """

    def __init__(self, name, parameters):
        super().__init__(name, parameters)
        self.stories = []

    def load_odt(self):
        pass
        # file = os.path.join(self.img_directory, "user_stories.odt")
        # textdoc = load(file)
        # allparas = textdoc.getElementsByType(text.P)
        # teletype.extractText(allparas[0])
        # print(teletype)

    def load_csv(self):
        """ Load user stories from a csv file """
        with open('assets/csv/user_stories.csv', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for line in reader:
                story = Story(line['Page'], line['Story'], line['Scenario'], line['Description'])
                self.stories.append(story)

    def generate_menu(self):

        self.pdf.set_font(self.font, '', 14)
        a_text = "LES USER STORIES AVEC CRITERES D'ACCEPTATION"
        self.pdf.text(x=5, y=45, txt=a_text)
        self.pdf.set_font(self.font, '', 12)
        a_text = "Les fonctionnalités"
        self.pdf.text(x=5, y=60, txt=a_text)

        fleche = os.path.join(self.img_directory, "fleche.jpg")

        table_of_content = [[2, 'page 2', "La page de connexion"],
                            [3, 'page 3', "La page interface de chat"],
                            [4, 'page 4', "La page du calendrier"],
                            [5, 'page 4', "La page de gestion des tâches"],
                            [6, 'page 4', "La page tableau de bord"]]

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

    def generate_p1(self):
        self.pdf.add_page()
        a_text = "La page de connexion"
        self.pdf.set_font(self.font, '', 14)
        self.pdf.set_text_color(218, 33, 33)
        self.pdf.text(x=10, y=10, txt=a_text)

        fleche = os.path.join(self.img_directory, "fleche.jpg")

        posy = 30
        self.pdf.set_text_color(0, 0, 0)
        save_story = ''

        for elem in self.stories:
            if elem.page == "La page de connexion":
                # draw the story
                if elem.story != save_story:
                    self.pdf.image(fleche, x=20, y=posy - 5, w=10, h=5)
                    self.pdf.set_font(self.font, '', 12)
                    self.pdf.text(x=30, y=posy, txt=elem.story)
                    posy += 13
                save_story = elem.story
                self.pdf.text(x=10, y=posy, txt=elem.scenario)
                self.pdf.text(x=10, y=posy, txt=elem.scenario)
                self.pdf.line(10, posy + 2, 10 + 200, posy + 2)
                posy += 10
                wrapper = textwrap.TextWrapper(width=140)
                word_list = wrapper.wrap(elem.description)
                for elem in word_list:
                    self.pdf.text(x=10, y=posy, txt=elem)
                    posy += 10
                posy += 15
                if posy >= 150:
                    self.generate_footer()
                    self.pdf.add_page()
                    posy = 30

    def generate(self):
        self.generate_header()

        self.generate_menu()
        self.generate_footer()

        self.generate_p1()
        self.generate_footer()

        self.generate_file()