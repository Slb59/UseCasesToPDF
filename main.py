from pdf.pdf import PDF
from litreview.litreview import litreview



if __name__ == "__main__":
    my_pdf = PDF(
        "litreview.pdf", "Critiques de livres"
    )
    litreview(my_pdf)
    my_pdf.generate_file()




