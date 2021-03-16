# -*- coding: utf-8 -*-
import socket
import psutil
import pickle

localIP = socket.gethostname()
localPort = 9991
bufferSize = 1024

msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

disk_info = psutil.disk_partitions(all=False)
bytes_to_send = pickle.dumps(disk_info)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0].decode('ascii')
    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    print(clientMsg)
    print(clientIP)

    UDPServerSocket.sendto(bytes_to_send, address)