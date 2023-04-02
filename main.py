from pdf.pdf import PDF
from tests.soutenance import soutenance_p7
from tests.diapositives import diapositives_p7



if __name__ == "__main__":
    # my_pdf = PDF(
    #     "soutenance-p7.pdf",
    #     "Projet n°7 : Résolvez des problèmes en utilisant des algorithmes en Python",
    # )
    # soutenance_p7(my_pdf)
    # my_pdf.generate_file()

    my_pdf = PDF(
        "diapositives.pdf", "AlgoInvest&Trade: Analyse d'un portefeuille d'actions"
    )
    diapositives_p7(my_pdf)
    my_pdf.generate_file()




