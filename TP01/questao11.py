# -*- coding: utf-8 -*-
import os
import errno


class Questao_11():
    """
    This program creates a process and opens a user-given text file.
    """

    def __init__(self):
        """ Constructor """
        self.search_path, self.error = '', ''
        self.file_name = 'text_file.txt'
        self.file_path = '.\\7'  # dado inexistente forçando input
        print('===' * 25, 'Questão 11'.center(75), '===' * 25, sep='\n')
        self.init_class()
        self.process_data()

    def init_class(self):
        """ This function receives the input data from users. """

        self.search_path = os.path.join(self.file_path, self.file_name)
        if os.path.exists(self.search_path):
            pass
        else:
            self.file_path = input(str('Digite o caminho de um arquivo: '))
            os.chdir(self.file_path)
            self.file_name = input('Digite o nome do arquivo: ')
            self.search_path = os.path.join(self.file_path, self.file_name)

    def process_data(self):
        """ This function process the input data from init_class. """
        if os.path.isfile(self.search_path):
            os.startfile(self.search_path)
        elif os.path.isdir(self.search_path):
            self.error = 'É um diretório!'
        else:
            self.error = FileNotFoundError(errno.ENOENT, os.strerror(
                errno.ENOENT), os.path.basename(self.search_path))

    def print_result(self):
        """ This is a printer! It prints. """
        if self.error:
            print(self.error)
        else:
            print('\nO arquivo {} foi aberto!'.format(self.file_name))


Questao_11().print_result()
