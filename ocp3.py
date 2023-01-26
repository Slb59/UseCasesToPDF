from app import OCP3, ArgParser


def main():
    args = ArgParser()
    the_parameters = args.read_parameters()
    my_app = OCP3(the_parameters)
    #my_app.usecase_connexion()
    my_app.generate_files()
    print(my_app)


if __name__ == '__main__':
    main()
