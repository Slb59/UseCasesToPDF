from pdf.pdf import PDF
from litreview.litreview import litreview

if __name__ == "__main__":
    my_pdf = PDF(
        "litreview.pdf",
        "Developpement d'un site de critiques de livres et d'articles"
    )
    litreview(my_pdf)
    my_pdf.generate_file()
