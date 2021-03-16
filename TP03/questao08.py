# -*- coding: utf-8 -*-
import os
import time
import socket
import psutil
import pickle
from psutil._common import bytes2human


msgFromClient = " Hello UDP Server"
bytesToSend = msgFromClient.encode('ascii')

serverAddressPort = (socket.gethostname(), 9991)
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

try:
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    _msg = pickle.loads(msgFromServer[0])

    templ = "%-17s %8s %8s %8s %5s%% %9s  %s"
    print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type",
                    "Mount"))
    for part in _msg:
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                continue
        usage = psutil.disk_usage(part.mountpoint)
        print(templ % (
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint))

except Exception as erro:
            print(str(erro))
