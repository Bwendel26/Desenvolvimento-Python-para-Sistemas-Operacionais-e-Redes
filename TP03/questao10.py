# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 03 **************************
*    Questao 10                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Desenvolvimento Python para Redes e             *
*                           Sistemas Operacionais                          *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_10.py                                   *
***************************************************************************/
"""


import socket
import sys
import os


class Questao_10():
    """ This is a TCP client program. """

    def __init__(self):
        """ Constructor """
        os.chdir(os.path.dirname(__file__))
        self.cwd = os.getcwd()
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_host = socket.gethostname()
        self.door = 8881
        self.file_name = input('Entre com o nome do arquivo: ')

        try:
            self.client_socket.connect((self.client_host, self.door))
            self.client_socket.send(self.file_name.encode('ascii'))
            msg = self.client_socket.recv(12)
            file_size = int(msg.decode('ascii'))
            if file_size >= 0:
                dowload_dir = self.cwd + '\\download\\'
                if not os.path.exists(dowload_dir):
                    os.mkdir(dowload_dir)
                _file = open(dowload_dir + self.file_name, 'wb')
                count = 0
                _bytes = self.client_socket.recv(4096)

                while _bytes:
                    _file.write(_bytes)
                    count = count + len(_bytes)
                    os.system('cls')
                    self.download_status(count, file_size)
                    _bytes = self.client_socket.recv(4096)
                _file.close()
            else:
                print('Arquivo não encontrado no servidor!')
        except Exception as err:
            print(str(err))
            self.client_socket.close()
        input("Pressione qualquer tecla para sair...")

    def download_status(self, _bytes, _size):
        """ Docstring """
        kbytes = _bytes/1024
        tam_bytes = _size/1024
        texto = 'Baixando... '
        texto = texto + '{:<.2f}'.format(kbytes) + ' KB '
        texto = texto + 'de ' + '{:<.2f}'.format(tam_bytes) + ' KB'
        print(texto)


Questao_10()
