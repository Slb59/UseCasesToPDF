import os
import textwrap
from datetime import datetime
from fpdf import FPDF
from functools import wraps


class PDF:
    def __init__(self, name, title):
        self.assets_folder = 'assets'
        self.font = 'Raleway-Light.ttf'
        # self.font="helvetica"
        self.name = name
        self.total_pages = 1
        self.current_page = 1
        self.pdf = FPDF(orientation='L', unit='mm', format='A4')
        file = os.path.join(self.assets_folder, self.font)
        self.pdf.add_font(self.font, '', file, uni=True)        
        self.center = 149
        self.title = title

    def generate_header(self, logo=True):
        """ generate the header for each pages """        
        self.pdf.add_page()
        if logo:            
            file = os.path.join(self.assets_folder, "logo-occ.png")
            self.pdf.image(file, x=5, y=5)        
        self.pdf.set_font(self.font, '', 14)
        self.pdf.text(x=90, y=10,txt=self.title)


    def generate_footer(self):
        """ generate the footer of the page """
        now = datetime.now()
        a_text = "Développeur d'application Python - Sylvie Bricout – Le "
        a_text += f"{now.day}/{now.strftime('%m')}/{now.year}"
        self.pdf.set_font(self.font, '', 12)
        self.pdf.text(x=70, y=205, txt=a_text)
        a_text = f"{self.current_page}/{self.total_pages}"
        self.pdf.text(x=270, y=205, txt=a_text)

    def generate_file(self):
        """ generate the file in the output directory """
        file = os.path.join('output', self.name)
        self.pdf.output(file)

    def add_title(self, a_text: str):
        self.pdf.set_font(self.font, '', 24)        
        self.pdf.text(x=self.center - (self.pdf.get_string_width(a_text)/2), y=30, txt=a_text)

    def page_img(self, img_name):
        """ generate a page with a image """
        self.generate_header()
        file = os.path.join(self.assets_folder, img_name)
        self.pdf.image(file, x=10, y=30, w=280, h=150)
        self.generate_footer()

    def add_paragraph(self, x, y, text, line_spacing=10) -> int:
        file = os.path.join(self.assets_folder, "fleche.jpg")
        self.pdf.image(file, x=x, y=y, w=20, h=10)
        y+=5
        wrapper = textwrap.TextWrapper(width=90)
        text_list = text.split('\n')
        for a_text in text_list:
            word_list = wrapper.wrap(text=a_text)
            for element in word_list:
                self.pdf.text(x=x+40, y=y, txt=element)
                y+=line_spacing
        return y
    
    def add_header_footer(self, ma_func, logo=False):    
        @wraps(ma_func)
        def wrapper_function(*args, **kwargs):
            self.generate_header(logo)
            result = ma_func(*args, **kwargs)
            self.generate_footer()
            return result

        return wrapper_function
    
    def display_table(self,x,y,data,col_width=10):
        
        line_height = self.pdf.font_size * 2
        self.pdf.set_xy(x,y)
        posy=y+line_height
        for row in data:
            for datum in row:
                self.pdf.multi_cell(col_width, line_height, datum, border=1, ln=3)
            self.pdf.set_xy(x,posy)
            posy += line_height


