# -*- coding: utf-8 -*-

import os
import psutil
from psutil._common import bytes2human


class Questao_20():
    """
    This program gets the logged username.
    """

    def __init__(self):
        """ Constructor """
        self.error = ''
        self.info_dict = dict()
        self.cwd = os.getcwd()
        self.partitions = psutil.disk_partitions()

        print('===' * 25, 'Questão 20'.center(75), '===' * 25, sep='\n')
        self.init_class()
        self.process_data()

    def init_class(self):
        """ This function receives the input data from users. """
        pass

    def process_data(self):
        """ This function process the input data from init_class. """

        for partition in range(len(self.partitions)):
            device = getattr(self.partitions[partition], 'device')
            mountpoint = getattr(self.partitions[partition], 'mountpoint')
            fstype = getattr(self.partitions[partition], 'fstype')
            self.usage = psutil.disk_usage(mountpoint)
            if self.cwd[:3] == device:
                self.info_dict['Dispositivo:'] = device
                self.info_dict['Sistema de arquivos:'] = fstype
                self.info_dict['Armazenamento total:'] = bytes2human(
                    getattr(self.usage, 'total'))
                self.info_dict['Armazenamento disponível:'] = bytes2human(
                    getattr(self.usage, 'free'))
            else:
                pass

    def print_result(self):
        """ This is a printer! It prints. """

        if self.error:
            print(self.error)
        else:
            for k, v in self.info_dict.items():
                print('{:<26} {:<10}'.format(k, v))


Questao_20().print_result()
