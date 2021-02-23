# -*- coding: utf-8 -*-

import os

user = ''
username = ''

def process_data():
    
    if hasattr(os, 'getlogin'):
        try:
            user = os.getlogin()
            if user:
                return user
        except OSError:
                pass
    if hasattr(os, 'getuid'):
        try:
            user = os.getuid()
            if user:
                return user
        except OSError:
            pass
    username = os.environ.get("USERNAME")
    if username:
        return username

    return 'Nome do usuário logado: '+ user if user else username


print(process_data())