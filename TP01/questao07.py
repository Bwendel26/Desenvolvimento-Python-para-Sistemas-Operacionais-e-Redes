# -*- coding: utf-8 -*-

import os
import errno


class Questao_07():

    def __init__(self):
        """ Constructor """
        self.search_path = ''
        self.is_file, self.is_directory, self.error = '', '', ''
        self.file_name = 'questao07.py'
        self.file_path = '.\\'
        print('===' * 25, 'Questão 07'.center(75), '===' * 25, sep='\n')
        self.init_class()
        self.process_data()

    def init_class(self):
        """ This function receives the input data from users. """
        if os.path.exists(self.file_path):
            self.search_path = os.path.join(self.file_path, self.file_name)
            return self.search_path
        else:
            self.file_path = input(str('Digite o caminho de um arquivo: '))
            self.file_name = input('Digite o nome do arquivo: ')
            self.search_path = os.path.join(self.file_path, self.file_name)
            return self.search_path

    def process_data(self):
        """ This function process the input data from init_class. """
        if os.path.isfile(self.search_path):
            self.abs_path = os.path.abspath(self.file_name)
            self.file_path = os.path.split(self.abs_path)
        elif os.path.isdir(self.search_path):
            self.is_directory = 'diretório'
        else:
            self.error = FileNotFoundError(errno.ENOENT, os.strerror(
                errno.ENOENT), os.path.basename(self.search_path))

    def print_result(self):
        """ This is a printer! It prints. """
        if self.error:
            print(self.error)
        else:
            print('\nO caminho absoluto do arquivo {} é:\n {}'.format(self.file_name,
                                                                self.file_path[0]))



Questao_07().print_result()
