import app
import argparse
from logs import LOGGER
from .parameters import Parameters


class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser('ocp3')

        self.parser.add_argument('--version', '-v',
                                 action='store_true',
                                 help='show current version')

        self.parser.add_argument('--output',
                                 type=str,
                                 help='set the output files directory')

        self.args = self.parser.parse_args()

        LOGGER.debug(self.args)

        if self.args.version:
            print('ocp3 ' + app.__version__)

    def read_parameters(self):

        p = Parameters()

        if self.args.output is not None:
            p.output_directory = self.args.output

        return p