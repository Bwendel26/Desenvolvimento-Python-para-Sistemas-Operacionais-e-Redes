# -*- coding: utf-8 -*-

import os
import psutil
from psutil._common import bytes2human


class Questao_18():
    """
    This program gets the total from virtual and swap memory.
    """

    def __init__(self):
        """ Constructor """
        self.error = ''
        self.virtual_memory = dict()
        self.swap_memory = dict()
        print('===' * 25, 'Questão 18'.center(75), '===' * 25, sep='\n')
        self.init_class()
        self.process_data()

    def init_class(self):
        """ This function receives the input data from users. """
        pass

    def process_data(self):
        """ This function process the input data from init_class. """
        for field in psutil.virtual_memory()._fields:
            if field == 'total':
                self.virtual_memory['total'] = bytes2human(
                    getattr(psutil.virtual_memory(), field))

        for field in psutil.swap_memory()._fields:
            if field == 'total':
                self.swap_memory['total'] = bytes2human(
                    getattr(psutil.swap_memory(), field))

    def print_result(self):
        """ This is a printer! It prints. """

        if self.error:
            print(self.error)
        else:
            print('Memória principal\n\tTotal: {:<10}\n'.format(self.virtual_memory['total']),
                  'Memória swap\n\tTotal: {:<10}'.format(self.swap_memory['total']))

Questao_18().print_result()
