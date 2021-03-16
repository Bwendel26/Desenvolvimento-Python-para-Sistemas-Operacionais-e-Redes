# -*- coding: utf-8 -*-
import socket
import os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = socket.gethostname()
door = 8881
server_socket.bind((server_host, door))
server_socket.listen()
print('\nServidor de nome {} esperando conexão na porta {}'.format(server_host, door))

while True:
    (socket_cliente, addr) = server_socket.accept()
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