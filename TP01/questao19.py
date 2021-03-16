# -*- coding: utf-8 -*-

import os
import psutil
from psutil._common import bytes2human


class Questao_19():
    """
    This program gets the logged username.
    """

    def __init__(self):
        """ Constructor """
        self.error = ''
        print('===' * 25, 'Questão 19'.center(75), '===' * 25, sep='\n')
        self.init_class()
        self.process_data()

    def init_class(self):
        """ This function receives the input data from users. """
        pass

    def process_data(self):
        """ This function process the input data from init_class. """
        self.partitions = psutil.disk_partitions()
        self.usage = psutil.disk_usage(self.partitions[0][0])

    def print_result(self):
        """ This is a printer! It prints. """

        if self.error:
            print(self.error)
        else:
            print('Partição do sistema {}\n\tArmazenamento disponível: {}'.format(
                self.partitions[0][0],
                bytes2human(self.usage[2])))


Questao_19().print_result()
