# -*- coding: utf-8 -*-

import os
import sys

platform = sys.platform
os_name = os.name
pid = ''

def process_data():

    if platform.startswith('linux'):
        pid = os.getgid()
    elif platform.startswith('win32'):
        pid = os.getpid()

    return 'Sistema operacional: '+ 'Windows' if platform == 'win32' else 'Linux' + '\nPID deste processo: ' + pid

print(process_data())