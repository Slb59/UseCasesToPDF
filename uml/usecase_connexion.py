import pygraphviz as pgv


class UseCaseConnexion:
    def __init__(self):
        path = 'assets/dot/connexion.dot'
        A = pgv.AGraph(path)
        A.layout()
        A.draw("output/uml-usecase_connexion.png")


