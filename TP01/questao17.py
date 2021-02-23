# -*- coding: utf-8 -*-

import os
import psutil
import time

class Questao_17():
    """
    This program gets the logged username.
    """

    def __init__(self):
        """ Constructor """
        self.error = ''
        self.times_cpu = list()
        print('===' * 25, 'Questão 17'.center(75), '===' * 25, sep='\n')
        self.init_class()
        self.process_data()

    def init_class(self):
        """ This function receives the input data from users. """
        pass

    def process_data(self):
        """ This function process the input data from init_class. """
        self.times_cpu = psutil.cpu_times_percent(interval=1, percpu=True)

    def print_result(self):
        """ This is a printer! It prints. """

        if self.error:
            print(self.error)
        else:
            print('Número de núcleos: {}\n'.format(len(self.times_cpu)))
            for i in range(20):
                print('Repetição número {}'.format(i+1))
                for core in range(len(self.times_cpu)):
                    print('{}Núcleo {}: user={} system={} idle={}'.format(
                        ' '*3,
                        core+1,
                        self.times_cpu[core][0],
                        self.times_cpu[core][1],
                        self.times_cpu[core][2]))
                time.sleep(1)


Questao_17().print_result()
