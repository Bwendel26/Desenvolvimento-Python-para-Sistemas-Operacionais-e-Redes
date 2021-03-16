# -*- coding: utf-8 -*-
"""
/************************ TESTE DE PERFORMANCE 03 **************************
*    Questao 11                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Desenvolvimento Python para Redes e             *
*                           Sistemas Operacionais                          *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_11.py                                   *
***************************************************************************/
"""
import socket
import os


class Questao_11():
    """ This is a TCP server program. """

    def __init__(self):
        """ Constructor """
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_host = socket.gethostname()
        self.door = 8881
        self.server_socket.bind((self.server_host, self.door))
        self.server_socket.listen()
        print('\nServidor de nome {} esperando conexão na porta {}'.format(
            self.server_host, self.door))

        while True:
            (socket_cliente, addr) = self.server_socket.accept()
            print("Conectado a:", str(addr))
            msg = socket_cliente.recv(2048)
            file_name = msg.decode('ascii')
            if os.path.isfile(file_name):
                file_size = os.stat(file_name).st_size
                socket_cliente.send(str(file_size).encode('ascii'))
                _file = open(file_name, 'rb')
                _bytes = _file.read(4096)
                while _bytes:
                    socket_cliente.send(_bytes)
                    _bytes = _file.read(4096)
                _file.close()
            else:
                print('Arquivo não encontrado!')
                socket_cliente.send('-1'.encode('ascii'))
            socket_cliente.close()


Questao_11()
