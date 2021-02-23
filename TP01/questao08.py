# -*- coding: utf-8 -*-
import os
from psutil._common import bytes2human
import errno


class Questao_08():
    """
    This program lists the files in a given directory.
    """

    def __init__(self):
        """ Constructor """
        self.search_path = '.\\'
        self.error = ''
        self.list_dir = list()
        self.list_file = list()
        print('===' * 25, 'Questão 08'.center(75), '===' * 25, sep='\n')
        self.init_class()
        self.process_data()

    def init_class(self):
        """ This function receives the input data from users. """
        
        if os.path.exists(self.search_path):
            self.list_dir = os.listdir(self.search_path)
        else:
            self.search_path = input(str('Digite o caminho de um diretório: '))
            os.chdir(self.search_path)
            self.list_dir = os.listdir(os.chdir(self.search_path))

    def process_data(self):
        """ This function process the input data from init_class. """
        for item in self.list_dir:
            if os.path.isfile(item):
                self.list_file.append(
                    [item, bytes2human(os.stat(item).st_size)])
            elif os.path.isdir(item):
                pass
            else:
                self.error = FileNotFoundError(errno.ENOENT, os.strerror(
                    errno.ENOENT), os.path.basename(item))

    def print_result(self):
        """ This is a printer! It prints. """
        if self.error:
            print(self.error)
        else:
            print('Conteúdo do diretório: \n {}'.format(os.path.abspath(self.search_path)),
                  '\t {:<15} {:^10}'.format('Arquivo', 'Tamanho'), sep="\n")
            for _file in self.list_file:
                print('\t {:<15} {:^10}'.format(_file[0], _file[1]))


Questao_08().print_result()
