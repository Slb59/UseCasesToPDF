from app import *


def main():
    args = ArgParser()
    the_parameters = args.read_parameters()
    my_app = OCP3(the_parameters)
    my_app.usecase_connexion()
    print(my_app)


if __name__ == '__main__':
    main()
