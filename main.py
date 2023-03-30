import os
from pdf.pdf import PDF
from tests.soutenance import soutenance_p7




class P7_2(PDF):

    def title(self, a_text: str):
        self.pdf.set_font(self.font, '', 24)
        self.pdf.text(x=self.center - (len(a_text)/2), y=50, txt=a_text)

    def add_page(self, nb: int):
        self.current_page = nb
        if nb == 1:
            self.page_img("mapmind.png")
        if nb == 2:
            self.page_context()
        if nb == 3:
            self.page3()
        if nb == 4:
            self.page4()
        if nb == 5:
            self.page5()
        if nb == 6:
            self.page6()
        if nb == 7:
            self.page7()       
        if nb == 8:
            self.page8()
        if nb== 9:
            self.page9()
        if nb == 10:
            self.page_conclude_diff()


    def page_context(self):
        self.generate_header()
        self.title('RAPPEL DU CONTEXT')
        file = os.path.join(self.assets_folder, "fleche.jpg")
        self.pdf.set_font(self.font, '', 20)
        posy = 70
        self.pdf.image(file, x=20, y=posy, w=20, h=10)
        a_text = "L’association souhaite se doter d’une application web permettant"         
        self.pdf.text(x=60, y=posy+10, txt=a_text)
        a_text = "de visualiser en temps réel un classement de films intéressants"
        self.pdf.text(x=60, y=posy+20, txt=a_text)
        self.pdf.image(file, x=20, y=posy+30, w=20, h=10)
        a_text = 'Se baser sur la maquette proposée'
        self.pdf.text(x=60, y=posy+40, txt=a_text)
        self.pdf.image(file, x=20, y=posy+60, w=20, h=10)
        a_text = 'Utiliser un API maison : OCMovies-API'
        self.pdf.text(x=60, y=posy+70, txt=a_text)
        self.generate_footer()

    def page3(self):
        self.generate_header()
        self.title("Démonstration de l'application")
        file = os.path.join(self.assets_folder, "fleche.jpg")
        self.pdf.set_font(self.font, '', 20)
        posy = 70
        self.pdf.image(file, x=20, y=posy, w=20, h=10)
        a_text = "La navigation, le meilleur film"
        self.pdf.text(x=60, y=posy + 10, txt=a_text)
        self.pdf.image(file, x=20, y=posy + 30, w=20, h=10)
        a_text = 'Les caroussels : défilements'
        self.pdf.text(x=60, y=posy + 40, txt=a_text)
        self.pdf.image(file, x=20, y=posy + 60, w=20, h=10)
        a_text = "La modal : via le bouton play, via n'importe quel film"
        self.pdf.text(x=60, y=posy + 70, txt=a_text)
        self.generate_footer()

    def page4(self):
        self.generate_header()
        self.title('METHODE DE TRAVAIL - Le Front')
        self.generate_footer()
        file = os.path.join(self.assets_folder, "front-end.png")
        self.pdf.set_font(self.font, '', 20)
        posy = 60
        self.pdf.image(file, x=20, y=posy, w=144, h=130)        
        self.generate_footer()

    def page5(self):
        self.generate_header()
        self.title('METHODE DE TRAVAIL - La modal')
        self.generate_footer()
        file = os.path.join(self.assets_folder, "modal.png")
        self.pdf.set_font(self.font, '', 20)
        posy = 70
        self.pdf.image(file, x=20, y=posy, w=135, h=100)        
        self.generate_footer()

    def page6(self):
        self.generate_header()
        self.title("Utilisation de l'API")
        self.generate_footer()
        file_arrow = os.path.join(self.assets_folder, "fleche.jpg")
        posy = 70
        self.pdf.image(file_arrow, x=20, y=posy, w=20, h=10)
        file = os.path.join(self.assets_folder, "fetch.png")
        self.pdf.image(file, x=50, y=posy, w=200)
        self.generate_footer()

    def page7(self):
        self.generate_header()
        self.title("Utilisation de l'API")
        file_arrow = os.path.join(self.assets_folder, "fleche.jpg")
        posy = 70
        self.pdf.image(file_arrow, x=20, y=posy, w=20, h=10)
        file = os.path.join(self.assets_folder, "fetch_all_best.png")
        self.pdf.image(file, x=50, y=posy)
        posy = 90
        self.pdf.image(file_arrow, x=20, y=posy, w=20, h=10)
        file = os.path.join(self.assets_folder, "fetch_best.png")
        self.pdf.image(file, x=50, y=posy)
        posy = 110
        self.pdf.image(file_arrow, x=20, y=posy, w=20, h=10)
        file = os.path.join(self.assets_folder, "fetch_genre.png")
        self.pdf.image(file, x=50, y=posy, w=230)
        self.generate_footer()

    def page8(self):
        self.generate_header()
        self.title("Gestion des styles avec sass")
        file = os.path.join(self.assets_folder, "structure sass.png")
        self.pdf.image(file, x=50, y=70)
        file = os.path.join(self.assets_folder, "style_scss.png")
        self.pdf.image(file, x=120, y=70)
        self.generate_footer()
    
    def page9(self):
        self.generate_header()
        self.title("Structure du javascript")
        file_arrow = os.path.join(self.assets_folder, "fleche.jpg")
        posy = 70
        self.pdf.image(file_arrow, x=20, y=posy, w=20, h=10)
        a_text = "main.js"
        self.pdf.text(x=60, y=posy + 10, txt=a_text)
        a_text = "  > affichage du meilleur film"
        self.pdf.text(x=60, y=posy + 20, txt=a_text)
        a_text = "  > chargement des images des caroussels"
        self.pdf.text(x=60, y=posy + 30, txt=a_text)
        a_text = "  > appel la gestion du scroll d'un caroussel"
        self.pdf.text(x=60, y=posy + 40, txt=a_text)
        a_text = "  > affichage de la modal"
        self.pdf.text(x=60, y=posy + 50, txt=a_text)
        a_text = "  > evenement click en dehors de la modal"
        self.pdf.text(x=60, y=posy + 60, txt=a_text)
        posy = 140
        self.pdf.image(file_arrow, x=20, y=posy, w=20, h=10)
        a_text = "caroussel.js"
        self.pdf.text(x=60, y=posy + 10, txt=a_text)
        a_text = "  > Genère le html"
        self.pdf.text(x=60, y=posy + 20, txt=a_text)
        a_text = "  > Chargement des images"
        self.pdf.text(x=60, y=posy + 30, txt=a_text)
        a_text = "  > Scroll selon une direction"
        self.pdf.text(x=60, y=posy + 40, txt=a_text)
        self.generate_footer()  

    def page_conclude_diff(self):
        self.generate_header()
        self.title('CONCLUSION')
        self.generate_footer()
        file = os.path.join(self.assets_folder, "fleche.jpg")
        self.pdf.set_font(self.font, '', 20)
        posy = 70
        self.pdf.image(file, x=20, y=posy, w=20, h=10)
        a_text = "Installation et utilisation de l'API"
        self.pdf.text(x=60, y=posy + 10, txt=a_text)
        self.pdf.image(file, x=20, y=posy + 30, w=20, h=10)
        a_text = 'HTML - CSS - JAVASCRIPT'
        self.pdf.text(x=60, y=posy + 40, txt=a_text)
        self.pdf.image(file, x=20, y=posy + 60, w=20, h=10)
        a_text = "Utilisation d'une structure SASS"
        self.pdf.text(x=60, y=posy + 70, txt=a_text)
        self.generate_footer()

    def page_conclude_up(self):
        self.generate_header()
        self.title('AXES D''AMELIORATION')
        self.generate_footer()
        file = os.path.join(self.assets_folder, "fleche.jpg")
        self.pdf.set_font(self.font, '', 20)
        posy = 70
        self.pdf.image(file, x=20, y=posy, w=20, h=10)
        a_text = ""
        self.pdf.text(x=60, y=posy + 10, txt=a_text)
        self.pdf.image(file, x=20, y=posy + 30, w=20, h=10)
        a_text = ''
        self.pdf.text(x=60, y=posy + 40, txt=a_text)
        self.pdf.image(file, x=20, y=posy + 60, w=20, h=10)
        a_text = ""
        self.pdf.text(x=60, y=posy + 70, txt=a_text)
        self.generate_footer()

    def page_img(self, img_name):
        self.generate_header()
        file = os.path.join(self.assets_folder, img_name)
        self.pdf.image(file, x=10, y=30, w=280, h=150)
        self.generate_footer()

if __name__ == '__main__':
    my_pdf = PDF('soutenance-p7.pdf',
                   "Projet n°7 : Résolvez des problèmes en utilisant des algorithmes en Python")
    soutenance_p7(my_pdf)
    my_pdf.generate_file()

    my_pdf = P7_2('diapositives.pdf',
                   "AlgoInvest&Trade: Analyse d'un portefeuille d'actions")
    my_pdf.total_pages = 1
    for iPage in range(my_pdf.total_pages):
        my_pdf.add_page(iPage+1)
    my_pdf.generate_file()



