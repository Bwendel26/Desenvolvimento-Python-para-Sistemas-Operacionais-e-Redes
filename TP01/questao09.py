# -*- coding: utf-8 -*-

import os
import time
import errno
from psutil._common import bytes2human


class Questao_09():
    """
    This program lists the file creation and modification dates from 
    files in a given directory.
    """

    def __init__(self):
        """ Constructor """
        self.search_path = '.\\'
        self.error = ''
        self.list_dir = list()
        self.list_file = list()
        print('===' * 25, 'Questão 09'.center(75), '===' * 25, sep='\n')
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
                    [item, time.ctime(os.stat(item).st_atime),
                                     time.ctime(os.stat(item).st_mtime)])
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
            print('Conteúdo do diretório: \n {}\n'.format(os.path.abspath(self.search_path)),
                  ' {:^30} {:^25} {:^25}'.format('Arquivo', 'Modificação', 'Criação'), sep="\n")
            for _file in self.list_file:
                print(' {:<30} {:^25} {:^25}'.format(_file[0], _file[1], _file[2]))


Questao_09().print_result()
