# -*- coding: utf-8 -*-
import os
import sys
import psutil
import time
from psutil._common import bytes2human


class Questao_15():
    """
    This program gets a PID from user and shows some info.
    """

    def __init__(self):
        """ Constructor """
        self.platform = sys.platform
        self.os_name = os.name
        self.pid = 0
        self.error = ''
        self.proc_info = dict()
        print('===' * 25, 'Questão 15'.center(75), '===' * 25, sep='\n')
        self.init_class()
        self.process_data()

    def init_class(self):
        """ This function receives the input data from users. """

        if self.platform.startswith('linux'):
            self.pid = input(
                'Digite o PID de um processo ou OK para o processo corrente: ').lower()
            if self.pid == 'ok':
                self.pid = os.getgid()
            else:
                pass

        elif self.platform.startswith('win32'):
            self.pid = input(
                'Digite o PID de um processo ou OK para o processo corrente: ').lower()
            if self.pid == 'ok':
                self.pid = os.getpid()
            else:
                pass
        else:
            self.error = 'Não compatível com este sistema operacional!'

    def process_data(self):
        """ This function process the input data from init_class. """
        if psutil.pid_exists(int(self.pid)):
            for proc in psutil.process_iter(['pid', 'name', 'username', 'memory_info', 'create_time']):
                if int(self.pid) == proc.info['pid']:
                    self.proc_info['PID do processo:'] = proc.info['pid']
                    self.proc_info['Nome do processo:'] = proc.info['name']
                    self.proc_info['Usuário Proprietário:'] = proc.info['username']
                    self.proc_info['Tempo de criação:'] = time.ctime(
                        proc.info['create_time'])
                    self.proc_info['Uso de memória:'] = str(
                        round(proc.info['memory_info'][0]/1000)) + ' Kb'
                    break
        else:
            self.error = 'O processo não existe!'
            self.init_class()

    def print_result(self):
        """ This is a printer! It prints. """

        if self.error:
            print(self.error)
        else:
            for k, v in self.proc_info.items():
                print('{}{:<22} {:<15}'.format(' '*3,k, v))


Questao_15().print_result()
