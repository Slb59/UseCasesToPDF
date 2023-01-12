from fpdf import FPDF
import os

def main():
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    cwd = os.path.dirname(__file__)
    file = os.path.join(cwd, "assets", "fonts", "Raleway-Light.ttf")
    pdf.add_font('Raleway-Light', '', file, uni=True)
    pdf.set_font('Raleway-Light', '', 10)
    pdf.set_text_color(255, 255, 255)
    file = os.path.join(cwd, "assets", "img", "logo_dev4u.png")
    pdf.image(file, x=0, y=0, w=50, h=25)
    file = os.path.join(cwd, "output", "test1.pdf")
    pdf.output(file)

if __name__ == '__main__':
    main()
